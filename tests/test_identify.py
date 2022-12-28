from unittest.mock import AsyncMock

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import pytest

from pysungrow import identify
from pysungrow.definitions.devices.hybrid import sh10rt
from pysungrow.definitions.variables.device import OutputType


@pytest.mark.asyncio
async def test_success():
    client = AsyncModbusTcpClient("127.0.0.1")
    client.connect = AsyncMock(return_value=(None, client))
    client.read_input_registers = AsyncMock(
        return_value=ReadInputRegistersResponse(
            [16690, 12854, 12854, 12854, 12854, 12854, 0, 0, 0, 0, 3587, 100, 1]
        )
    )

    result = await identify(client)
    assert result == ("A22626262626", sh10rt, OutputType.THREE_PHASE_3P4L)
