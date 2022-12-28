"""Functions for reading from Modbus clients."""

from typing import Any, Dict, List

from pymodbus.client import ModbusBaseClient

from pysungrow.definitions.variable import VariableDefinition, VariableType
from pysungrow.lib.decode import decode_variables
from pysungrow.lib.group_variables_by_proximity import group_variables_by_proximity


async def read_variables(
    client: ModbusBaseClient, variables: List[VariableDefinition], slave: int
) -> Dict[str, Any]:
    """
    Read some registers from a client.

    Batches register read requests together for better efficiency and decodes the results.

    :param client: The client from which to read
    :param variables: The registers that should be read
    :param slave: The unit/slave from which to read
    :return: The read and decoded registers
    """
    input_groups = group_variables_by_proximity(
        [
            r
            for r in variables
            if r.variable_type in (VariableType.READ, VariableType.READ_STATIC)
        ]
    )
    holding_groups = group_variables_by_proximity(
        [r for r in variables if r.variable_type == VariableType.READWRITE]
    )

    result: Dict[str, Any] = {}
    for group in input_groups:
        # note: communication address = protocol address - 1
        response = await client.read_input_registers(
            group[0].address - 1,
            count=group[-1].end_address - group[0].address + 1,
            slave=slave,
        )
        result.update(decode_variables(response.registers, group))
    for group in holding_groups:
        # note: communication address = protocol address - 1
        response = await client.read_holding_registers(
            group[0].address - 1,
            count=group[-1].end_address - group[0].address + 1,
            slave=slave,
        )
        result.update(decode_variables(response.registers, group))
    return result
