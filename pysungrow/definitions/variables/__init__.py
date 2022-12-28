from typing import List

from pysungrow.definitions.variable import VariableDefinition

from . import device, general, hybrid, string

variables: List[VariableDefinition] = [
    v
    for module in [device, general, hybrid, string]
    for v in module.__dict__.values()
    if isinstance(v, VariableDefinition)
]
