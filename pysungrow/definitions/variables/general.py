from datetime import datetime
from enum import Enum

from pysungrow.definitions.devices.hybrid import all_hybrid
from pysungrow.definitions.devices.string import (
    all_string,
    sg33ktl_m,
    sg36ktl_m,
    sg40ktl_m,
    sg49k5j,
    sg50ktl_m,
    sg60ktl_m,
    sg60ku_m,
    sg80ktl_m,
)
from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.definitions.variables.device import OutputType

daily_output_energy_variable_5003 = VariableDefinition(
    VariableType.READ,
    "daily_output_energy",
    5003,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices={*all_string, *all_hybrid},
)
total_output_energy_variable_5004 = VariableDefinition(
    VariableType.READ,
    "total_output_energy",
    5004,
    RawType.U32,
    int,
    unit="kWh",
    devices={*all_string, *all_hybrid},
)
total_running_time_variable_5006 = VariableDefinition(
    VariableType.READ,
    "total_running_time",
    5006,
    RawType.U32,
    int,
    unit="h",
    devices={*all_string},
)
internal_temperature_variable_5008 = VariableDefinition(
    VariableType.READ,
    "internal_temperature",
    5008,
    RawType.S16,
    float,
    transform=0.1,
    unit="°C",
    devices={*all_string, *all_hybrid},
)


mppt_1_voltage_variable_5011 = VariableDefinition(
    VariableType.READ,
    "mppt_1_voltage",
    5011,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={*all_hybrid},
)
mppt_1_current_variable_5012 = VariableDefinition(
    VariableType.READ,
    "mppt_1_current",
    5012,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={*all_hybrid},
)
mppt_2_voltage_variable_5013 = VariableDefinition(
    VariableType.READ,
    "mppt_2_voltage",
    5013,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={*all_hybrid},
)
mppt_2_current_variable_5014 = VariableDefinition(
    VariableType.READ,
    "mppt_2_current",
    5014,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={*all_hybrid},
)
dc_1_voltage_variable_5011 = VariableDefinition(
    VariableType.READ,
    "dc_1_voltage",
    5011,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={*all_string},
)
dc_1_current_variable_5012 = VariableDefinition(
    VariableType.READ,
    "dc_1_current",
    5012,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={*all_string},
)
dc_2_voltage_variable_5013 = VariableDefinition(
    VariableType.READ,
    "dc_2_voltage",
    5013,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={
        sg33ktl_m,
        sg40ktl_m,
        sg50ktl_m,
        sg60ktl_m,
        sg60ku_m,
        sg49k5j,
        sg80ktl_m,
        sg36ktl_m,
    },
)
dc_2_current_variable_5014 = VariableDefinition(
    VariableType.READ,
    "dc_2_current",
    5014,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={
        sg33ktl_m,
        sg40ktl_m,
        sg50ktl_m,
        sg60ktl_m,
        sg60ku_m,
        sg49k5j,
        sg80ktl_m,
        sg36ktl_m,
    },
)
dc_3_voltage_variable_5015 = VariableDefinition(
    VariableType.READ,
    "dc_3_voltage",
    5015,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={
        sg33ktl_m,
        sg40ktl_m,
        sg50ktl_m,
        sg60ktl_m,
        sg60ku_m,
        sg49k5j,
        sg80ktl_m,
        sg36ktl_m,
    },
)
dc_3_current_variable_5016 = VariableDefinition(
    VariableType.READ,
    "dc_3_current",
    5016,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={
        sg33ktl_m,
        sg40ktl_m,
        sg50ktl_m,
        sg60ktl_m,
        sg60ku_m,
        sg49k5j,
        sg80ktl_m,
        sg36ktl_m,
    },
)
dc_4_voltage_variable_5115 = VariableDefinition(
    VariableType.READ,
    "dc_4_voltage",
    5115,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={sg49k5j, sg50ktl_m, sg60ktl_m, sg60ku_m, sg80ktl_m},
)
dc_4_current_variable_5116 = VariableDefinition(
    VariableType.READ,
    "dc_4_current",
    5116,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={sg49k5j, sg50ktl_m, sg60ktl_m, sg60ku_m, sg80ktl_m},
)
total_dc_power_variable_5017 = VariableDefinition(
    VariableType.READ,
    "total_dc_power",
    5017,
    RawType.U32,
    int,
    unit="W",
    devices={*all_string, *all_hybrid},
)
phase_a_voltage_variable_5019 = VariableDefinition(
    VariableType.READ,
    "phase_a_voltage",
    5019,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.SINGLE_PHASE, OutputType.THREE_PHASE_3P4L},
    devices={*all_string, *all_hybrid},
)
phase_b_voltage_variable_5020 = VariableDefinition(
    VariableType.READ,
    "phase_b_voltage",
    5020,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.THREE_PHASE_3P4L},
    devices={*all_string, *all_hybrid},
)
phase_c_voltage_variable_5021 = VariableDefinition(
    VariableType.READ,
    "phase_c_voltage",
    5021,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.THREE_PHASE_3P4L},
    devices={*all_string, *all_hybrid},
)
line_ab_voltage_variable_5019 = VariableDefinition(
    VariableType.READ,
    "line_ab_voltage",
    5019,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.THREE_PHASE_3P3L},
    description="A-B line voltage",
    devices={*all_string, *all_hybrid},
)
line_bc_voltage_variable_5020 = VariableDefinition(
    VariableType.READ,
    "line_bc_voltage",
    5020,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.THREE_PHASE_3P3L},
    description="B-C line voltage",
    devices={*all_string, *all_hybrid},
)
line_ca_voltage_variable_5021 = VariableDefinition(
    VariableType.READ,
    "line_ca_voltage",
    5021,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    if_output_type={OutputType.THREE_PHASE_3P3L},
    description="C-A line voltage",
    devices={*all_string, *all_hybrid},
)
phase_a_current_variable_5022 = VariableDefinition(
    VariableType.READ,
    "phase_a_current",
    5022,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices={*all_string},
)
phase_b_current_variable_5023 = VariableDefinition(
    VariableType.READ,
    "phase_b_current",
    5023,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    if_output_type={OutputType.THREE_PHASE_3P4L, OutputType.THREE_PHASE_3P3L},
    devices={*all_string},
)
phase_c_current_variable_5024 = VariableDefinition(
    VariableType.READ,
    "phase_c_current",
    5024,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    if_output_type={OutputType.THREE_PHASE_3P4L, OutputType.THREE_PHASE_3P3L},
    devices={*all_string},
)
total_active_power_variable_5031 = VariableDefinition(
    VariableType.READ,
    "total_active_power",
    5031,
    RawType.U32,
    int,
    unit="W",
    devices={*all_string},
)
reactive_power_variable_5033 = VariableDefinition(
    VariableType.READ,
    "reactive_power",
    5033,
    RawType.S32,
    int,
    unit="var",
    devices={*all_string, *all_hybrid},
)
power_factor_variable_5035 = VariableDefinition(
    VariableType.READ,
    "power_factor",
    5035,
    RawType.S16,
    float,
    transform=0.001,
    devices={*all_string, *all_hybrid},
)
grid_frequency_variable_5036 = VariableDefinition(
    VariableType.READ,
    "grid_frequency",
    5036,
    RawType.U16,
    float,
    transform=0.1,
    unit="Hz",
    devices={*all_string, *all_hybrid},
)

system_clock_variable_5000 = VariableDefinition(
    VariableType.READWRITE,
    "system_clock",
    5000,
    RawType.RAW,
    datetime,
    transform=(
        lambda raw: datetime(
            year=raw[0],
            month=raw[1],
            day=raw[2],
            hour=raw[3],
            minute=raw[4],
            second=raw[5],
        )
        if isinstance(raw, tuple)
        else None,
        lambda dt: (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second),
    ),
    length=6,
    devices={*all_string, *all_hybrid},
)


class StartStop(Enum):
    START = 0xCF
    STOP = 0xCE
    EMERGENCY_STOP = 0xBB
