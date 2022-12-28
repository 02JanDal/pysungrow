from unittest.mock import AsyncMock

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.register_read_message import ReadInputRegistersResponse
import pytest

from pysungrow import SungrowClient
from pysungrow.definitions.devices.hybrid import sh10rt
from pysungrow.definitions.variables.device import OutputType


@pytest.mark.asyncio
async def test_accessors():
    client = SungrowClient(
        AsyncModbusTcpClient("127.0.0.1"), sh10rt, OutputType.THREE_PHASE_3P4L
    )
    assert client.device == sh10rt
    assert len(client.keys) > 20
    assert client.variable("output_type").type == OutputType


@pytest.mark.asyncio
async def test_get():
    mb_client = AsyncModbusTcpClient("127.0.0.1")
    mb_client.connect = AsyncMock(return_value=(None, mb_client))
    mb_client.read_input_registers = AsyncMock(
        return_value=ReadInputRegistersResponse([0x1234])
    )
    client = SungrowClient(mb_client, sh10rt, OutputType.THREE_PHASE_3P4L)
    assert "nominal_output_power" not in client.data
    await client.refresh(["nominal_output_power"])
    mb_client.read_input_registers.assert_awaited_once_with(5000, count=1, slave=1)
    assert client.data["nominal_output_power"] == 466.0
    client.refresh = AsyncMock()
    assert await client.get("nominal_output_power") == 466.0
    # since we already have the value it should not be refreshed again
    client.refresh.assert_not_awaited()


@pytest.mark.asyncio
async def test_get_invalid_key():
    client = SungrowClient(
        AsyncModbusTcpClient("127.0.0.1"), sh10rt, OutputType.THREE_PHASE_3P4L
    )
    with pytest.raises(KeyError):
        await client.get("foo_bar")


@pytest.mark.asyncio
async def test_set():
    mb_client = AsyncModbusTcpClient("127.0.0.1")
    mb_client.connect = AsyncMock(return_value=(None, mb_client))
    mb_client.read_holding_registers = AsyncMock(
        return_value=ReadInputRegistersResponse([0x1234])
    )
    mb_client.write_registers = AsyncMock()
    client = SungrowClient(mb_client, sh10rt, OutputType.THREE_PHASE_3P4L)
    await client.set("charge_discharge", 100)
    mb_client.write_registers.assert_awaited_once()
    mb_client.read_holding_registers.assert_awaited_once()


@pytest.mark.asyncio
async def test_set_invalid_key():
    client = SungrowClient(
        AsyncModbusTcpClient("127.0.0.1"), sh10rt, OutputType.THREE_PHASE_3P4L
    )
    with pytest.raises(KeyError):
        await client.set("foo_bar", 2)


@pytest.mark.asyncio
async def test_set_invalid_key_is_readonly():
    client = SungrowClient(
        AsyncModbusTcpClient("127.0.0.1"), sh10rt, OutputType.THREE_PHASE_3P4L
    )
    with pytest.raises(KeyError):
        await client.set("output_type", 2)


@pytest.mark.asyncio
async def test_set_invalid_value_type():
    client = SungrowClient(
        AsyncModbusTcpClient("127.0.0.1"), sh10rt, OutputType.THREE_PHASE_3P4L
    )
    with pytest.raises(ValueError):
        await client.set("off_grid_enabled", 2)
