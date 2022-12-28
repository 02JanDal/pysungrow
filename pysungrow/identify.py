"""Identifying the type/model of inverter."""

from typing import Tuple

from pymodbus.client import ModbusBaseClient
from pymodbus.exceptions import ModbusException

from pysungrow.definitions.device import SungrowDevice
from pysungrow.definitions.variables.device import (
    OutputType,
    device_type_variable_5000,
    output_type_variable_5002,
    serial_number_variable_4990,
)
from pysungrow.lib.read_variables import read_variables


class NotASungrowDeviceException(BaseException):
    """Thrown when attempting to communicate with a device that is not recognized as a Sungrow inverter."""


async def identify(
    client: ModbusBaseClient, slave: int = 1
) -> Tuple[str, SungrowDevice, OutputType]:
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
        return result["serial_number"], result["device_type"], result["output_type"]
    except ModbusException:
        raise NotASungrowDeviceException()
    finally:
        await conn.close()
