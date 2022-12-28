"""Main access point for connecting to inverters."""

from typing import Any, Dict, List, Optional, Sequence

from pymodbus.client.base import ModbusBaseClient

from pysungrow.definitions.device import SungrowDevice
from pysungrow.definitions.variable import VariableDefinition, VariableType
from pysungrow.definitions.variables import variables
from pysungrow.definitions.variables.device import OutputType
from pysungrow.lib.read_variables import read_variables
from pysungrow.lib.write_variable import write_variable


class SungrowClient:
    """Provides access to variables of the given device. Caches fetched values."""

    def __init__(
        self,
        client: ModbusBaseClient,
        device: SungrowDevice,
        output_type: OutputType,
        slave: int = 1,
    ):
        """
        Construct a client for communicating with Sungrow inverters.

        :param client: The Modbus client over which communication takes place
        :param device: The Sungrow device model which will be communicated with, controls the available variables
        :param output_type: The output type configured for the inverter, controls some available variables
        :param slave: The unit/slave to connect to
        """
        self._client = client
        self._device = device
        self._output_type = output_type
        self._slave = slave
        self._data: Dict[str, Any] = {}

    @property
    def device(self) -> SungrowDevice:
        """Device type connected to."""
        return self._device

    @property
    def data(self) -> Dict[str, Any]:
        """Access to cached data."""
        return self._data

    @property
    def _variables(self):
        return (
            r
            for r in variables
            if self._device in r.devices
            and (r.if_output_type is None or self._output_type in r.if_output_type)
        )

    @property
    def keys(self) -> List[str]:
        """All keys available for the device."""
        return [r.key for r in self._variables]

    def variable(self, key: str) -> Optional[VariableDefinition]:
        """
        Retrieve the variable definition of a variable given its key.

        :param key: Key of the variable
        :return: The variable definition
        """
        return next((r for r in self._variables if r.key == key), None)

    def _variable_should_refresh(
        self, keys: Optional[Sequence[str]], variable: VariableDefinition
    ):
        if keys is not None and variable.key not in keys:
            return False
        if (
            variable.variable_type == VariableType.READ_STATIC
            and variable.key in self._data
        ):
            return False
        return True

    async def refresh(self, keys: Optional[Sequence[str]] = None):
        """
        Refresh the cached values of variables for the device.

        :param keys: Optionally restrict the variables to refresh to this set
        """
        _, conn = await self._client.connect()
        try:
            await self._refresh_impl(conn, keys)
        finally:
            await conn.close()

    async def _refresh_impl(
        self, conn: ModbusBaseClient, keys: Optional[Sequence[str]]
    ):
        self._data.update(
            await read_variables(
                conn,
                [v for v in self._variables if self._variable_should_refresh(keys, v)],
                self._slave,
            )
        )

    async def get(self, key: str) -> Any:
        """
        Retrieve the (cached) value for a variable with the given key. Fetches data if no cached value is available.

        :param key: The key of the variable to retrieve
        :return: The (cached) value
        """
        if key not in self.keys:
            raise KeyError("The given key is not available in this device")
        if key not in self._data:
            await self.refresh()
        return self._data[key]

    async def set(self, key: str, value: Any):
        """
        Set the value of the variable with the given key.

        :param key: Key of the variable to set
        :param value: New value
        """
        variable = self.variable(key)
        if not variable:
            raise KeyError("The given key is not available in this device")
        elif variable.variable_type != VariableType.READWRITE:
            raise KeyError("Given key is not writeable")
        elif variable.type != type(value):
            raise ValueError(f"Value for given key must be of type {variable.type}")

        _, conn = await self._client.connect()
        try:
            await write_variable(conn, value, variable, self._slave)
            await self._refresh_impl(conn, [key])
        finally:
            await conn.close()
