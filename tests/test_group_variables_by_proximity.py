from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.group_variables_by_proximity import group_variables_by_proximity

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


def test_group_one():
    assert group_variables_by_proximity([var_1]) == [[var_1]]


def test_group_large():
    assert group_variables_by_proximity([var_1, var_2, var_5, var_10]) == [
        [var_1, var_2, var_5, var_10]
    ]


def test_group_medium():
    assert group_variables_by_proximity([var_1, var_2, var_5, var_10], 4) == [
        [var_1, var_2, var_5],
        [var_10],
    ]


def test_group_small():
    assert group_variables_by_proximity([var_1, var_2, var_5, var_10], 1) == [
        [var_1, var_2],
        [var_5],
        [var_10],
    ]
