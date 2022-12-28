from argparse import ArgumentParser
import asyncio
from enum import Enum

from pymodbus.client import AsyncModbusTcpClient

from pysungrow import SungrowClient, identify
from pysungrow.definitions.device import SungrowDevice


async def do_identify(host, port, slave):
    client = AsyncModbusTcpClient(host, port)
    serial_number, device, output_type = await identify(client, slave)
    print("Serial number:", serial_number)
    print("Device:", device.name)
    print("Output type:", output_type.name)


async def do_get(host, port, slave, keys):
    client = AsyncModbusTcpClient(host, port)
    _, device, output_type = await identify(client, slave)
    sungrow = SungrowClient(client, device, output_type, slave)
    await sungrow.refresh()
    for key in sungrow.keys:
        if keys is not None and key not in keys:
            continue

        value = await sungrow.get(key)
        if isinstance(value, SungrowDevice):
            value = value.name
        unit = sungrow.variable(key).unit
        print(key + ":", f"{value} {unit}" if unit is not None else value)


async def do_set(host, port, slave, key, value):
    client = AsyncModbusTcpClient(host, port)
    _, device, output_type = await identify(client, slave)
    sungrow = SungrowClient(client, device, output_type, slave)

    variable = sungrow.variable(key)
    if variable.type in (int, float):
        value = variable.type(value)
    elif issubclass(variable.type, Enum):
        value = variable.type[value]
    elif variable.type == bool:
        if value.lower() == "true" or value == "1":
            value = True
        elif value.lower() == "false" or value == "0":
            value = False
        else:
            raise ValueError(
                "Value for boolean types must be one of 'true', 'false', '1' or '0'"
            )

    old = await sungrow.get(key)
    unit = variable.unit
    print("Current value:", f"{old} {unit}" if unit is not None else old)
    print("Setting value:", f"{value} {unit}" if unit is not None else value)
    await sungrow.set(key, value)
    new = await sungrow.get(key)
    print("New value:", f"{new} {unit}" if unit is not None else new)


parser = ArgumentParser(prog="pysungrow")
parser.add_argument("host")
parser.add_argument("-p", "--port", type=int, default=502)
parser.add_argument("-s", "--slave", type=int, default=1)

subparsers = parser.add_subparsers()
parser_identify = subparsers.add_parser("identify")
parser_identify.set_defaults(
    func=lambda arg: asyncio.run(do_identify(arg.host, arg.port, arg.slave))
)
parser_get = subparsers.add_parser("get")
parser_get.add_argument("-k", "--key", action="append")
parser_get.set_defaults(
    func=lambda arg: asyncio.run(do_get(arg.host, arg.port, arg.slave, arg.key))
)
parser_set = subparsers.add_parser("set")
parser_set.add_argument("key")
parser_set.add_argument("value")
parser_set.set_defaults(
    func=lambda arg: asyncio.run(
        do_set(arg.host, arg.port, arg.slave, arg.key, arg.value)
    )
)

args = parser.parse_args()
args.func(args)
