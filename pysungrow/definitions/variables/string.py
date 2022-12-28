from datetime import datetime, timedelta
from enum import Enum

from pysungrow.definitions.devices.string import (
    all_string,
    sg8ktl_m,
    sg10ktl_m,
    sg12ktl_m,
    sg33ktl_m,
    sg36ktl_m,
    sg40ktl_m,
    sg49k5j,
    sg50ktl_m,
    sg60ktl,
    sg60ktl_m,
    sg60ku,
    sg60ku_m,
    sg80hv,
    sg80ktl,
    sg80ktl_m,
    sg125hv,
)
from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.definitions.variables.general import StartStop

grid_frequency_variable_5148 = VariableDefinition(
    VariableType.READ,
    "grid_frequency_fine",
    5148,
    RawType.U16,
    float,
    transform=0.01,
    unit="Hz",
    devices={sg8ktl_m, sg10ktl_m, sg12ktl_m, sg80ktl_m, sg80hv, sg125hv},
)


class SystemState(Enum):
    RUNNING = 0x0
    STOP = 0x8000
    STOP_KEY = 0x1300
    STOP_EMERGENCY = 0x1500
    STANDBY = 0x1400
    INITIAL_STANDBY = 0x1200
    STARTUP = 0x1600
    RUNNING_ALARM = 0x9100
    RUNNING_DERATING = 0x8100
    RUNNING_DISPATCH = 0x8200
    RUNNING_FAULT = 0x5500
    COMMUNICATE_FAULT = 0x2500


system_state_variable_5038 = VariableDefinition(
    VariableType.READ,
    "system_state",
    5038,
    RawType.U16,
    SystemState,
    devices=all_string,
)
fault_date_variable_5039 = VariableDefinition(
    VariableType.READ,
    "fault_date",
    5039,
    RawType.RAW,
    datetime,
    transform=lambda raw: datetime(
        year=raw[0], month=raw[1], day=raw[2], hour=raw[3], minute=raw[4], second=raw[5]
    )
    if isinstance(raw, tuple) and raw[0] > 0
    else None,
    length=6,
    devices={*all_string},
)
fault_code_variable_5045 = VariableDefinition(
    VariableType.READ, "fault_code", 5045, RawType.U16, int, devices={*all_string}
)
nominal_reactive_output_power_variable_5049 = VariableDefinition(
    VariableType.READ,
    "nominal_reactive_output_power",
    5049,
    RawType.U16,
    float,
    transform=0.1,
    unit="K var",
    devices={*all_string},
)
impedance_to_ground_variable_5071 = VariableDefinition(
    VariableType.READ,
    "impedance_to_ground",
    5071,
    RawType.U16,
    int,
    unit="kΩ",
    devices={*all_string},
)
work_state_variable_5081 = VariableDefinition(
    VariableType.READ, "work_state2", 5081, RawType.U32, int, devices={*all_string}
)
daily_running_time_variable_5113 = VariableDefinition(
    VariableType.READ,
    "daily_running_time",
    5113,
    RawType.U16,
    timedelta,
    transform=lambda minutes: timedelta(minutes=minutes)
    if isinstance(minutes, int)
    else None,
    devices={*all_string},
)


class CountryCode(Enum):
    GB = 0
    DE = 1
    FR = 2
    IT = 3
    ES = 4
    AT = 5
    AU = 6
    CZ = 7
    BE = 8
    DK = 9
    GR_L = 10
    GR_IS = 11
    NL = 12
    PT = 13
    CHN = 14
    SE = 15
    OTHER_50HZ = 16
    RO = 17
    TH = 18
    TK = 19
    AU_WEST = 20
    VORARLBERG_AUSTRIA = 25
    CA = 60
    US = 61
    OTHER_60HZ = 62
    JP_50HZ = 70
    JP_60HZ = 71


country_variable_5114 = VariableDefinition(
    VariableType.READ_STATIC,
    "country",
    5114,
    RawType.U16,
    CountryCode,
    transform=CountryCode,
    devices={*all_string},
)
monthly_power_yield_variable_5128 = VariableDefinition(
    VariableType.READ,
    "monthly_power_yield",
    5128,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices={*all_string},
)
negative_voltage_to_ground_5146 = VariableDefinition(
    VariableType.READ,
    "negative_voltage_to_ground",
    5146,
    RawType.S16,
    float,
    transform=0.1,
    unit="V",
    devices={*all_string},
)
bus_voltage_variable_5147 = VariableDefinition(
    VariableType.READ,
    "bus_voltage",
    5147,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices={*all_string},
)

start_stop_variable_5006 = VariableDefinition(
    VariableType.READWRITE,
    "start_stop",
    5006,
    RawType.U16,
    StartStop,
    devices=all_string,
)
power_limitation_variable_5007 = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation",
    5007,
    RawType.U16,
    bool,
    transform=(lambda raw: raw == 0xAA, lambda val: 0xAA if val else 0x55),
    devices=all_string,
)
power_limitation_setting_variable_5008_a = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_setting",
    5008,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    limits=(0, 110),
    devices={
        sg50ktl_m,
        sg60ktl_m,
        sg60ktl,
        sg60ku_m,
        sg60ku,
        sg33ktl_m,
        sg40ktl_m,
        sg80ktl_m,
    },
)
power_limitation_setting_variable_5008_b = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_setting",
    5008,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    limits=(0, 100),
    devices={sg49k5j, sg36ktl_m, sg10ktl_m, sg12ktl_m, sg80ktl, sg125hv},
)
power_factor_setting_variable_5019 = VariableDefinition(
    VariableType.READWRITE,
    "power_factor_setting",
    5019,
    RawType.S16,
    float,
    transform=0.001,
    limits=(-1, 1),
    devices=all_string,
)


class ReactivePowerAdjustment(Enum):
    OFF = 0x55
    SET_POWER_FACTOR = 0xA1
    SET_REACTIVE_PERCENTAGE = 0xA2
    ENABLE_QP_CURVE = 0xA3
    ENABLE_QU_CURVE = 0xA4


reactive_power_adjustment_switch_variable_5036 = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment_switch",
    5036,
    RawType.U16,
    ReactivePowerAdjustment,
    devices=all_string,
)
reactive_power_percentage_variable_5037 = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_percentage",
    5037,
    RawType.S16,
    float,
    transform=0.1,
    unit="%",
    limits=(-100.0, 100.0),
    devices=all_string,
)
power_limitation_adjustment_variable_5039_a = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 55.0),
    devices={sg50ktl_m},
)
power_limitation_adjustment_variable_5039_b = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 66.0),
    devices={sg60ktl_m, sg60ku_m, sg60ktl, sg60ku},
)
power_limitation_adjustment_variable_5039_c = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 49.5),
    devices={sg49k5j},
)
power_limitation_adjustment_variable_5039_d = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 36.3),
    devices={sg33ktl_m},
)
power_limitation_adjustment_variable_5039_e = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 44.0),
    devices={sg40ktl_m},
)
power_limitation_adjustment_variable_5039_f = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 88.0),
    devices={sg80ktl_m},
)
power_limitation_adjustment_variable_5039_g = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 36.0),
    devices={sg36ktl_m},
)
power_limitation_adjustment_variable_5039_h = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 10.0),
    devices={sg10ktl_m},
)
power_limitation_adjustment_variable_5039_i = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 12.0),
    devices={sg125hv},
)
power_limitation_adjustment_variable_5039_j = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 80.0),
    devices={sg80ktl},
)
power_limitation_adjustment_variable_5039_k = VariableDefinition(
    VariableType.READWRITE,
    "power_limitation_adjustment",
    5039,
    RawType.U16,
    float,
    transform=0.1,
    unit="kW",
    limits=(0.0, 125.0),
    devices={sg125hv},
)
reactive_power_adjustment_variable_5040_a = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-25.0, 25.0),
    devices={sg50ktl_m},
)
reactive_power_adjustment_variable_5040_b = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-30.0, 30.0),
    devices={sg60ktl_m, sg60ku_m, sg60ktl, sg60ku},
)
reactive_power_adjustment_variable_5040_c = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-24.7, 24.7),
    devices={sg49k5j},
)
reactive_power_adjustment_variable_5040_d = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-16.5, 16.5),
    devices={sg33ktl_m},
)
reactive_power_adjustment_variable_5040_e = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-20.0, 20.0),
    devices={sg40ktl_m},
)
reactive_power_adjustment_variable_5040_f = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-18.0, 18.0),
    devices={sg36ktl_m},
)
reactive_power_adjustment_variable_5040_g = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-5.0, 5.0),
    devices={sg10ktl_m},
)
reactive_power_adjustment_variable_5040_h = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-6.0, 6.0),
    devices={sg12ktl_m},
)
reactive_power_adjustment_variable_5040_i = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-40.0, 40.0),
    devices={sg80ktl, sg80ktl_m},
)
reactive_power_adjustment_variable_5040_j = VariableDefinition(
    VariableType.READWRITE,
    "reactive_power_adjustment",
    5040,
    RawType.S16,
    float,
    transform=0.1,
    unit="K var",
    limits=(-62.0, 62.0),
    devices={sg125hv},
)
