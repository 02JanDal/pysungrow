"""Functions for decoding data from registers."""

import math
from typing import Any, Dict, List, Optional, Tuple, TypeVar, Union, cast

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder

from pysungrow.definitions.variable import RawType, VariableDefinition

T = TypeVar("T")


def decode_registers_for_variable(
    decoder: BinaryPayloadDecoder, variable: VariableDefinition[T]
) -> Optional[T]:
    """
    Decode the information for the given variable.

    First decodes the raw data (which controls the number of registers used) before doing any
    additional transforms to Python data types.

    :param decoder: Decoder that contains the data, positioned at the start of the given register
    :param variable: The register for which to decode information
    :return: The decoded value
    """
    raw: Union[int, str, Tuple[int, ...]]
    if variable.raw_type == RawType.U16:
        raw = decoder.decode_16bit_uint()
    elif variable.raw_type == RawType.U32:
        raw = decoder.decode_32bit_uint()
    elif variable.raw_type == RawType.S16:
        raw = decoder.decode_16bit_int()
    elif variable.raw_type == RawType.S32:
        raw = decoder.decode_32bit_int()
    elif variable.raw_type == RawType.STRING:
        assert variable.length is not None
        raw = decoder.decode_string(variable.length * 2).decode("utf-8")
        if isinstance(raw, str) and "\x00" in raw:
            raw = raw[0 : raw.find("\x00")]
    elif variable.raw_type == RawType.RAW:
        raw = tuple(
            cast(int, decoder.decode_16bit_uint()) for _ in range(variable.length or 1)
        )
    else:  # pragma: no cover
        raise KeyError("Unknown raw type")

    if (
        isinstance(variable.transform, float)
        and variable.type == float
        and isinstance(raw, int)
    ):
        value = float(raw) * variable.transform

        # calculate number of decimals after the point based on scale (0.1 -> 1, 0.01 -> 2)
        after_point = -math.log10(variable.transform)
        # if the number of decimals is a whole number we can use it for rounding
        if after_point == round(after_point):
            value = round(value, int(after_point))

        return value  # type: ignore
    elif isinstance(variable.transform, int):
        return int(raw) * variable.transform
    elif isinstance(variable.transform, tuple):
        return variable.transform[0](raw)
    elif callable(variable.transform):
        return variable.transform(raw)  # type: ignore
    else:
        # also handles the case where register.transform is set to an enum
        return variable.type(raw)  # type: ignore


def decode_variables(
    data: List[int], variables: List[VariableDefinition]
) -> Dict[str, Any]:
    """
    Decode information for all variables fetched in a single read.

    :param data: The raw data as returned by pymodbus; a sequence of words (as in the 2 byte data type)
    :param variables: The variables for which the data was fetched
    :return: The decoded data for all passed registers
    """
    decoder = BinaryPayloadDecoder.fromRegisters(
        data, wordorder=Endian.Little, byteorder=Endian.Big
    )
    current = variables[0].address
    result: Dict[str, Any] = {}
    for variable in variables:
        skip = variable.address - current
        if skip > 0:
            decoder.skip_bytes(skip * 2)
        result[variable.key] = decode_registers_for_variable(decoder, variable)
        current = variable.end_address + 1
    return result
