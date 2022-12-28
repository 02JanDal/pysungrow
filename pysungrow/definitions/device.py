"""Classes for defining a Sungrow inverter."""

from dataclasses import dataclass
from enum import Enum


class SungrowDeviceType(str, Enum):
    """Type of inverter."""

    HYBRID = "Hybrid"
    STRING = "String"


@dataclass
class SungrowDevice:
    """Basic definition of a Sungrow inverter."""

    code: int
    name: str
    device_type: SungrowDeviceType

    def __hash__(self):
        return self.code
