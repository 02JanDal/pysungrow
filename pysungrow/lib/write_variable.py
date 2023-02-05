"""Functions for writing to Modbus clients."""

from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    try:
        from pymodbus.client.base import ModbusBaseClient
    except ImportError:
        # support for pymodbus v2.5.3
        from pymodbus.client.asynchronous.mixins import (
            BaseAsyncModbusClient as ModbusBaseClient,
        )

from pysungrow.definitions.variable import VariableDefinition, VariableType
from pysungrow.lib.encode import encode_registers_for_variable

T = TypeVar("T")


async def write_variable(
    client: "ModbusBaseClient", data: T, variable: VariableDefinition[T], slave: int
):
    """
    Write some data to a client.

    :param client: Client to which registers are written
    :param data: Data to write
    :param variable: Variable to write
    :param slave: Unit/slave to which registers are written
    """
    assert variable.variable_type == VariableType.READWRITE
    registers = encode_registers_for_variable(data, variable)
    # note: communication address = protocol address - 1
    await client.write_registers(variable.address - 1, registers, slave=slave)
