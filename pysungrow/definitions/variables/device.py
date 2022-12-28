from enum import Enum
from typing import Optional, Tuple, Union

from pysungrow.definitions.device import SungrowDevice
from pysungrow.definitions.devices.hybrid import all_hybrid
from pysungrow.definitions.devices.string import (
    all_string,
    sg8ktl_m,
    sg10ktl_m,
    sg12ktl_m,
    sg80ktl_m,
    sg125hv,
)
from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType


def _get_sungrow_device(
    code: Union[int, str, Tuple[int, ...]]
) -> Optional[SungrowDevice]:
    assert isinstance(code, int)

    from pysungrow.definitions.devices import devices

    return next((d for d in devices if d.code == code), None)


protocol_number_variable_4950 = VariableDefinition(
    VariableType.READ_STATIC,
    "protocol_number",
    4950,
    RawType.U32,
    int,
    devices={*all_string, *all_hybrid},
)
protocol_version_variable_4952 = VariableDefinition(
    VariableType.READ_STATIC,
    "protocol_version",
    4952,
    RawType.U32,
    int,
    devices={*all_string, *all_hybrid},
)
arm_software_version_variable_4954 = VariableDefinition(
    VariableType.READ_STATIC,
    "arm_software_version",
    4954,
    RawType.STRING,
    str,
    length=15,
    devices={sg8ktl_m, sg10ktl_m, sg12ktl_m, sg80ktl_m, sg125hv, *all_hybrid},
)
dsp_software_version_variable_4969 = VariableDefinition(
    VariableType.READ_STATIC,
    "dsp_software_version",
    4969,
    RawType.STRING,
    str,
    length=15,
    devices={sg8ktl_m, sg10ktl_m, sg12ktl_m, sg80ktl_m, sg125hv, *all_hybrid},
)
serial_number_variable_4990 = VariableDefinition(
    VariableType.READ_STATIC,
    "serial_number",
    4990,
    RawType.STRING,
    str,
    length=10,
    devices={*all_string, *all_hybrid},
)
device_type_variable_5000 = VariableDefinition(
    VariableType.READ_STATIC,
    "device_type",
    5000,
    RawType.U16,
    SungrowDevice,
    transform=_get_sungrow_device,
    devices={*all_string, *all_hybrid},
)
nominal_output_power_variable_5001 = VariableDefinition(
    VariableType.READ_STATIC,
    "nominal_output_power",
    5001,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    devices={*all_string, *all_hybrid},
)


class OutputType(Enum):
    """The output type of an inverter, as configured."""

    SINGLE_PHASE = 0
    THREE_PHASE_3P4L = 1
    THREE_PHASE_3P3L = 2


output_type_variable_5002 = VariableDefinition(
    VariableType.READ_STATIC,
    "output_type",
    5002,
    RawType.U16,
    OutputType,
    transform=OutputType,
    devices={*all_string, *all_hybrid},
)
