"""Functions for encoding data to registers."""

from enum import Enum
from typing import List, Tuple, TypeVar, Union

from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadBuilder

from pysungrow.definitions.variable import RawType, VariableDefinition

T = TypeVar("T")


def encode_registers_for_variable(
    data: T, variable: VariableDefinition[T]
) -> List[int]:
    """
    Encode the Python-native data of a variable to Modbus registers.

    :param data: The Python-native data to encode
    :param variable: Description of how the data should be encoded
    :return: The resulting registers
    """
    if variable.type != type(data):
        raise TypeError()

    builder = BinaryPayloadBuilder(wordorder=Endian.Little, byteorder=Endian.Big)

    raw: Union[int, str, Tuple[int, ...]]
    if isinstance(variable.transform, tuple):
        raw = variable.transform[1](data)
    elif isinstance(variable.transform, (float, int)) and variable.type in (float, int):
        assert isinstance(data, (float, int))
        raw = int(round(data / variable.transform))
    elif variable.type in (float, int):
        assert isinstance(data, (float, int))
        raw = int(round(data))
    elif issubclass(variable.type, Enum):
        assert variable.type == type(data)
        raw = data.value
    elif isinstance(data, int) and variable.raw_type in (
        RawType.U16,
        RawType.U32,
        RawType.S16,
        RawType.S32,
    ):
        raw = data
    else:  # pragma: no cover
        raise ValueError("Cannot encode data")

    if variable.raw_type == RawType.U16:
        builder.add_16bit_uint(raw)
    elif variable.raw_type == RawType.U32:
        builder.add_32bit_uint(raw)
    elif variable.raw_type == RawType.S16:
        builder.add_16bit_int(raw)
    elif variable.raw_type == RawType.S32:
        builder.add_32bit_int(raw)
    elif variable.raw_type == RawType.STRING:
        raise NotImplementedError()
    elif variable.raw_type == RawType.RAW:
        assert variable.length is not None
        if not isinstance(raw, tuple):
            raise TypeError()
        for word in raw:
            builder.add_16bit_uint(word)
    else:  # pragma: no cover
        raise KeyError("Unknown raw type")

    return builder.to_registers()
