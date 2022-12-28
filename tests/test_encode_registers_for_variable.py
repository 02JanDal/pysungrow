from enum import Enum

import pytest

from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.encode import encode_registers_for_variable


@pytest.mark.parametrize(
    "raw_type,data,result",
    [
        (RawType.U16, 62482, [0xF412]),
        (RawType.S16, -3054, [0xF412]),
        (RawType.U32, 4094851158, [0x7856, 0xF412]),
        (RawType.S32, -200116138, [0x7856, 0xF412]),
    ],
)
def test_various_ints(raw_type, data, result):
    assert (
        encode_registers_for_variable(
            data,
            VariableDefinition(
                VariableType.READ, "test", 1, raw_type, int, devices=set()
            ),
        )
        == result
    )


def test_float_no_transform():
    assert encode_registers_for_variable(
        15.0,
        VariableDefinition(
            VariableType.READ, "test", 1, RawType.U16, float, devices=set()
        ),
    ) == [0x000F]


def test_float_transform():
    assert encode_registers_for_variable(
        1.5,
        VariableDefinition(
            VariableType.READ,
            "test",
            1,
            RawType.U16,
            float,
            transform=0.1,
            devices=set(),
        ),
    ) == [0x000F]


def test_int_transform():
    assert encode_registers_for_variable(
        150,
        VariableDefinition(
            VariableType.READ, "test", 1, RawType.U16, int, transform=10, devices=set()
        ),
    ) == [0x000F]


def test_raw_transform_readwrite():
    assert encode_registers_for_variable(
        0x1234,
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
    ) == [0x1234, 0x5678]


class IntTestEnum(Enum):
    FOO = 0
    BAR = 1


def test_enum_int():
    assert encode_registers_for_variable(
        IntTestEnum.BAR,
        VariableDefinition(
            VariableType.READ, "test", 1, RawType.U16, IntTestEnum, devices=set()
        ),
    ) == [0x0001]
