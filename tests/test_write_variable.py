from unittest.mock import AsyncMock

from pymodbus.client import AsyncModbusTcpClient
import pytest

from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.lib.write_variable import write_variable


@pytest.mark.asyncio
async def test_write_encoded_int():
    client = AsyncModbusTcpClient("127.0.0.1")
    client.write_registers = AsyncMock()
    await write_variable(
        client,
        15,
        VariableDefinition(
            VariableType.READWRITE, "test", 3, RawType.U16, int, devices=set()
        ),
        1,
    )
    client.write_registers.assert_awaited_once_with(2, [0x000F], slave=1)
