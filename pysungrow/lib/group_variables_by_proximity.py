"""Function to group variables for batching."""

from typing import List

from pysungrow.definitions.variable import VariableDefinition


def group_variables_by_proximity(
    variables: List[VariableDefinition], max_distance: int = 100
) -> List[List[VariableDefinition]]:
    """
    Group variables together if they are within a given number of addresses between each other.

    Used to batch register read calls together.

    :param variables: The registers that should be grouped
    :param max_distance: The maximum distance between registers to be put into the same group.
    :return: List of groups of registers
    """
    groups: List[List[VariableDefinition]] = [[]]
    variables = sorted(variables, key=lambda r: r.address)
    for variable in variables:
        if (
            len(groups[-1]) > 0
            and (variable.address - groups[-1][-1].end_address) > max_distance
        ):
            groups.append([])
        groups[-1].append(variable)
    if len(groups[-1]) == 0:
        groups.pop()
    return groups
