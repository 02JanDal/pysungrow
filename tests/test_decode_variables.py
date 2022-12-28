from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.decode import decode_variables

var_1 = VariableDefinition(
    VariableType.READ, "var_1", 1, RawType.U16, int, devices=set()
)
var_2 = VariableDefinition(
    VariableType.READ, "var_2", 2, RawType.U16, int, devices=set()
)
var_5 = VariableDefinition(
    VariableType.READ, "var_5", 5, RawType.U16, int, devices=set()
)
var_10 = VariableDefinition(
    VariableType.READ, "var_10", 10, RawType.U16, int, devices=set()
)


def test_decode_one():
    assert decode_variables([0x1234], [var_1]) == dict(var_1=4660)


def test_decode_two():
    assert decode_variables([0x1234, 0x5678], [var_1, var_2]) == dict(
        var_1=4660, var_2=22136
    )


def test_decode_with_skip():
    assert decode_variables(
        [0x1234, 0x0000, 0x0000, 0x0000, 0x5678], [var_1, var_5]
    ) == dict(var_1=4660, var_5=22136)
