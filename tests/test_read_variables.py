from unittest.mock import AsyncMock

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.register_read_message import (
    ReadHoldingRegistersResponse,
    ReadInputRegistersResponse,
)
import pytest

from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.read_variables import read_variables


@pytest.mark.asyncio
async def test_read_one():
    client = AsyncModbusTcpClient("127.0.0.1")
    client.read_input_registers = AsyncMock(
        return_value=ReadInputRegistersResponse([0x1234])
    )
    client.read_holding_registers = AsyncMock()
    assert await read_variables(
        client,
        [
            VariableDefinition(
                VariableType.READ, "test", 3, RawType.U16, int, devices=set()
            )
        ],
        1,
    ) == dict(test=4660)
    client.read_input_registers.assert_awaited_once_with(2, count=1, slave=1)


@pytest.mark.asyncio
async def test_read_multiple():
    client = AsyncModbusTcpClient("127.0.0.1")
    client.read_input_registers = AsyncMock(
        return_value=ReadInputRegistersResponse([0x1234, 0x0000, 0x5678])
    )
    client.read_holding_registers = AsyncMock()
    assert await read_variables(
        client,
        [
            VariableDefinition(
                VariableType.READ, "test1", 3, RawType.U16, int, devices=set()
            ),
            VariableDefinition(
                VariableType.READ, "test2", 5, RawType.U16, int, devices=set()
            ),
        ],
        1,
    ) == dict(test1=4660, test2=22136)
    client.read_input_registers.assert_awaited_once_with(2, count=3, slave=1)


@pytest.mark.asyncio
async def test_read_input_and_holding():
    client = AsyncModbusTcpClient("127.0.0.1")
    client.read_input_registers = AsyncMock(
        return_value=ReadInputRegistersResponse([0x1234])
    )
    client.read_holding_registers = AsyncMock(
        return_value=ReadHoldingRegistersResponse([0x5678])
    )
    assert await read_variables(
        client,
        [
            VariableDefinition(
                VariableType.READ, "test1", 3, RawType.U16, int, devices=set()
            ),
            VariableDefinition(
                VariableType.READWRITE, "test2", 5, RawType.U16, int, devices=set()
            ),
        ],
        1,
    ) == dict(test1=4660, test2=22136)
    client.read_input_registers.assert_awaited_once_with(2, count=1, slave=1)
    client.read_holding_registers.assert_awaited_once_with(4, count=1, slave=1)
