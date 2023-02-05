"""Identifying the type/model of inverter."""
from typing import TYPE_CHECKING, List, NamedTuple, Union

from pymodbus.exceptions import ModbusException, ModbusIOException

if TYPE_CHECKING:
    try:
        from pymodbus.client.base import ModbusBaseClient
    except ImportError:
        # support for pymodbus v2.5.3
        from pymodbus.client.asynchronous.mixins import BaseAsyncModbusClient

        from pysungrow.compat import AsyncModbusTcpClient

        ModbusBaseClient = Union[BaseAsyncModbusClient, AsyncModbusTcpClient]

from pysungrow.definitions.device import SungrowDevice
from pysungrow.definitions.variables.device import (
    OutputType,
    arm_software_version_variable_4954,
    device_type_variable_5000,
    dsp_software_version_variable_4969,
    output_type_variable_5002,
    serial_number_variable_4990,
)
from pysungrow.lib.read_variables import read_variables


class NotASungrowDeviceException(BaseException):
    """Thrown when attempting to communicate with a device that is not recognized as a Sungrow inverter."""


class SungrowIdentificationResult(NamedTuple):
    """The result returned from the identify function."""

    serial_number: str
    device: SungrowDevice
    output_type: OutputType
    excluded_variables: List[str]


async def identify(
    client: "ModbusBaseClient", slave: int = 1
) -> SungrowIdentificationResult:
    """
    Identify the Sungrow device to which the client is connected.

    :param client: Modbus client with which to connect
    :param slave: Unit/slave identifier
    :return: Tuple of serial number, device and output type
    """
    _, conn = await client.connect()
    try:
        result = await read_variables(
            conn,
            [
                serial_number_variable_4990,
                device_type_variable_5000,
                output_type_variable_5002,
            ],
            slave,
        )

        # accessing the software versions is not possible when connected to the WiNet-S
        # while it's still possible to read a span covering these (for example, 4949-5000), we get an error in pymodbus
        # when attempting to starting on/in either of these (so 4953-4982)
        try:
            await read_variables(
                conn,
                [
                    arm_software_version_variable_4954,
                    dsp_software_version_variable_4969,
                ],
                slave,
            )
            has_software_versions = True
        except ModbusIOException:
            has_software_versions = False

        return SungrowIdentificationResult(
            result["serial_number"],
            result["device_type"],
            result["output_type"],
            ["arm_software_version", "dsp_software_version"]
            if not has_software_versions
            else [],
        )
    except ModbusException:
        raise NotASungrowDeviceException()
    finally:
        await conn.close()
