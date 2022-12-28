# pysungrow - Python interface to Sungrow inverters

![PyPI](https://img.shields.io/pypi/v/pysungrow)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pysungrow)
![PyPI - Status](https://img.shields.io/pypi/status/pysungrow)
![GitHub](https://img.shields.io/github/license/02jandal/pysungrow)
[![CI](https://github.com/02JanDal/pysungrow/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/02JanDal/pysungrow/actions/workflows/ci.yaml)

This Python package provides abstractions over the Modbus protocol used by inverters of the brand Sungrow.

## Features

- Both getting and setting data
- Fully async
- Fully typed
- Supports most forms of Modbus (TCP, UDP, TLS and Serial)
- (Theoretically) supports most Sungrow inverters, both string and hybrid
- High test coverage

## Supported inverters

**Tested:** SH10RT

**In theory:** SG60KTL, SG60KU, SG33KTL-M, SG36KTL-M, SG40KTL-M, SG50KTL-M, SG60KTL-M, SG60KU-M, SG49K5J, SG8KTL-M, SG10KTL-M, SG12KTL-M, SG80KTL, SG80KTL-M, SG80HV, SG125HV, SH5K-20, SH3K6, SH4K6, SH5K-V13, SH5K-30, SH3K6-30, SH4K6-30, SH5.0RS, SH3.6RS, SH4.6RS, SH6.0RS, SH8.0RT, SH6.0RT, SH5.0RT

Do you have an inverter that's not been tested yet? Please follow the instructions under _Getting started_ including running the `get` command, and report the result in a [new issue](https://github.com/02JanDal/pysungrow/issues/new).

## Getting started

Install using `pip`:

```bash
pip install pysungrow
```

See below for usaging from Python. Also comes with a simple command line interface:

```
pysungrow [-p PORT] [-s SLAVE] [HOST] identify
pysungrow [-p PORT] [-s SLAVE] [HOST] get [-k KEY]
pysungrow [-p PORT] [-s SLAVE] [HOST] set [KEY] [VALUE]
```

It is recommended to start using these commands to verify that you can connect to your inverter successfully.

## Usage

### Getting data from the inverter

```python
from pysungrow import identify, SungrowClient
from pymodbus.client import AsyncModbusTcpClient

async def example_get():
    modbus_client = AsyncModbusTcpClient("192.168.1.228")

    # first we need to identify the model of inverter...
    serial_number, device, output_type = await identify(modbus_client)

    # ...then we can create a client...
    client = SungrowClient(modbus_client, device, output_type)

    # ...using which we can get data
    return await client.get("total_dc_power")
```

Note that the first call to `client.get` will fetch all variables defined for your model of inverter. You can limit this by first manually triggering a fetch using `await client.refresh(["total_dc_power"])`.

### Controlling the inverter

```python
from pysungrow import identify, SungrowClient
from pysungrow.definitions.variables.hybrid import ChargeDischargeCommand
from pymodbus.client import AsyncModbusTcpClient

async def example_set():
    modbus_client = AsyncModbusTcpClient("192.168.1.228")

    # first we need to identify the model of inverter...
    serial_number, device, output_type = await identify(modbus_client)

    # ...then we can create a client...
    client = SungrowClient(modbus_client, device, output_type)

    # ...using which we can control the inverter
    await client.set("charge_discharge_command", ChargeDischargeCommand.CHARGE)
```

## Contributing

Contributions are always welcome!

For code contributions please make sure that all automated checks pass. The easiest way to do this is using these commands:

```bash
pre-commit run --all-files
pytest
```
## Acknowledgements

There are a few other similar projects available (however neither of them fit my needs):

 - [SungrowInverter](https://github.com/mvandersteen/SungrowInverter) by @mvandersteen
 - [HomeAssistant Modbus mappings](https://github.com/mkaiser/Sungrow-SHx-Inverter-Modbus-Home-Assistant) by @mkaiser
 - [sungrow-websocket](https://github.com/wallento/sungrow-websocket) by @wallento
 
## License

[MIT](https://choosealicense.com/licenses/mit/)
