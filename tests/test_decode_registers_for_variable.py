from enum import Enum

from pymodbus.payload import BinaryPayloadDecoder
import pytest

from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.decode import decode_registers_for_variable


@pytest.mark.parametrize(
    "raw_type,result",
    [
        (RawType.U16, 62482),
        (RawType.S16, -3054),
        (RawType.U32, 4094851158),
        (RawType.S32, -200116138),
    ],
)
def test_various_ints(raw_type, result):
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x12F4, 0x5678]),
            VariableDefinition(
                VariableType.READ, "test", 1, raw_type, int, devices=set()
            ),
        )
        == result
    )


def test_string_full_length():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x6261, 0x7200]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.STRING,
                str,
                length=4,
                devices=set(),
            ),
        )
        == "bar"
    )


def test_string_smaller():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x6261, 0x7200, 0x0000]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.STRING,
                str,
                length=6,
                devices=set(),
            ),
        )
        == "bar"
    )


def test_string_empty():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x0000, 0x0000]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.STRING,
                str,
                length=4,
                devices=set(),
            ),
        )
        == ""
    )


def test_float_no_transform():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x0F00]),
            VariableDefinition(
                VariableType.READ, "test", 1, RawType.U16, float, devices=set()
            ),
        )
        == 15
    )


def test_float_transform():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x0F00]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.U16,
                float,
                transform=0.1,
                devices=set(),
            ),
        )
        == 1.5
    )


def test_int_transform():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x0F00]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.U16,
                int,
                transform=10,
                devices=set(),
            ),
        )
        == 150
    )


def test_raw_transform_readonly():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x1234, 0x5678]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.RAW,
                int,
                length=2,
                transform=lambda raw: raw[0] * raw[1],
                devices=set(),
            ),
        )
        == 0x3412 * 0x7856
    )


def test_raw_transform_readwrite():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x1234, 0x5678]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.RAW,
                int,
                length=2,
                transform=(lambda raw: raw[0] * raw[1], lambda val: (val, 0x5678)),
                devices=set(),
            ),
        )
        == 0x3412 * 0x7856
    )


class IntTestEnum(Enum):
    FOO = 0
    BAR = 1


def test_enum_int():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x0100]),
            VariableDefinition(
                VariableType.READ, "test", 1, RawType.U16, IntTestEnum, devices=set()
            ),
        )
        == IntTestEnum.BAR
    )


class StringTestEnum(Enum):
    FOO = "foo"
    BAR = "bar"


def test_enum_str():
    assert (
        decode_registers_for_variable(
            BinaryPayloadDecoder.fromRegisters([0x6261, 0x7200]),
            VariableDefinition(
                VariableType.READ,
                "test",
                1,
                RawType.STRING,
                StringTestEnum,
                length=4,
                devices=set(),
            ),
        )
        == StringTestEnum.BAR
    )
