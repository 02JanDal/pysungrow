"""Classes for defining a variable provided by a Sungrow inverter."""

from dataclasses import dataclass
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Callable,
    Generic,
    Literal,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from pysungrow.definitions.device import SungrowDevice

if TYPE_CHECKING:
    from pysungrow.definitions.variables.device import OutputType


class RawType(str, Enum):
    """
    The "raw" type of data in a register (or sequence of registers).

    Can be further refined using the `transform` on the register (sequence).
    """

    U16 = "U16"
    U32 = "U32"
    S16 = "S16"
    S32 = "S32"
    STRING = "STRING"  # UTF-8
    RAW = "RAW"


class VariableType(str, Enum):
    """
    The type of variable.

    Can be:
    * Read-only (input register)
    * Read-only static (input register, doesn't change)
    * Read-write (holding register)
    """

    READ_STATIC = "READ_STATIC"
    READ = "READ"
    READWRITE = "READWRITE"


T = TypeVar("T")


@dataclass
class VariableDefinition(Generic[T]):
    """
    Stores information about a variable provided by a Sungrow inverter.

    Variables are stored in one or a consecutive sequence of registers (input or holding).

    This class contains the following information:
        * Metadata (`key`, `description`, `unit`)
        * Register address (`variable_type`, `address`)
        * Decoding/encoding instructions (`raw_type`, `type`, `transform`, `length`)
    """

    variable_type: VariableType
    key: str
    address: int
    raw_type: RawType
    type: Type[T]
    devices: Set[SungrowDevice]
    transform: Union[
        Type[T],
        float,
        Callable[[Union[int, str, Tuple[int, ...]]], Optional[T]],
        Tuple[
            Callable[[Union[int, str, Tuple[int, ...]]], Optional[T]],
            Callable[[T], Union[int, str, Tuple[int, ...]]],
        ],
        None,
    ] = None
    description: Optional[str] = None
    unit: Optional[
        Literal[
            "V",
            "A",
            "W",
            "kW",
            "Wh",
            "kWh",
            "°C",
            "Hz",
            "var",
            "K var",
            "kΩ",
            "%",
            "h",
            "s",
            "min",
            "kg",
            "Ah",
        ]
    ] = None
    length: Optional[int] = None
    limits: Optional[Union[Tuple[int, int], Tuple[float, float]]] = None
    if_output_type: Optional[Set["OutputType"]] = None

    @property
    def end_address(self):
        """Last register address which this variable covers."""
        return (
            self.address
            + {
                RawType.U16: 1,
                RawType.U32: 2,
                RawType.S16: 1,
                RawType.S32: 2,
                RawType.STRING: self.length,
                RawType.RAW: self.length,
            }[self.raw_type]
            - 1
        )
