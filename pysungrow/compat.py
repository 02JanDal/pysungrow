"""Import AsyncModbusTcpClient from this file to get a pymodbus 2/3 compatible class."""


try:
    from pymodbus.client import AsyncModbusTcpClient
except (ImportError, ModuleNotFoundError):
    # support for pymodbus v2.5.3
    from pymodbus.client.sync import ModbusTcpClient
    from pymodbus.exceptions import ModbusException

    class AsyncModbusTcpClient:  # type: ignore
        """Some glue to make pymodbus 2 look like pymodbus 3."""

        def __init__(self, host: str, port: int, **kwargs):
            #            self._loop = asyncio.get_event_loop()
            #            self._client = ReconnectingAsyncioModbusTcpClient(None, self._loop, **kwargs)
            #            self._coro = self._client.start(host, port)
            self._client = ModbusTcpClient(host, port, **kwargs)

        async def connect(self):
            self._client.connect()
            #            await self._coro
            #            if self._client.protocol is None:
            #                raise ConnectionRefusedError()
            return None, self

        async def close(self):
            self._client.close()

        #            self._client.stop()

        async def write_registers(self, *args, slave: int, **kwargs):
            self._client.write_registers(*args, unit=slave, **kwargs)

        #            await self._client.protocol.write_registers(*args, unit=slave, **kwargs)

        async def read_input_registers(self, *args, slave: int, **kwargs):
            resp = self._client.read_input_registers(*args, unit=slave, **kwargs)
            #            resp = await self._client.protocol.read_input_registers(
            #                *args, unit=slave, **kwargs
            #            )
            if isinstance(resp, ModbusException):
                raise resp
            return resp

        async def read_holding_registers(self, *args, slave: int, **kwargs):
            resp = self._client.read_holding_registers(*args, unit=slave, **kwargs)
            #            resp = await self._client.protocol.read_holding_registers(
            #                *args, unit=slave, **kwargs
            #            )
            if isinstance(resp, ModbusException):
                raise resp
            return resp
