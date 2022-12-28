from datetime import time
from enum import Enum
from typing import Optional

from pysungrow.definitions.devices.hybrid import (
    all_hybrid,
    sh3k6,
    sh3k6_30,
    sh4k6,
    sh4k6_30,
    sh5_0rt,
    sh5k_20,
    sh5k_30,
    sh5k_v13,
    sh6_0rt,
    sh8_0rt,
    sh10rt,
)
from pysungrow.definitions.variable import RawType, VariableDefinition, VariableType
from pysungrow.definitions.variables.device import OutputType
from pysungrow.definitions.variables.general import StartStop
from pysungrow.lib.flag import Flag


class SystemState(Enum):
    STOP = 0x0002
    STANDBY = 0x0008
    INITIAL_STANDBY = 0x0010
    STARTUP = 0x0020
    RUNNING = 0x0040
    FAULT = 0x0100
    RUNNING_MAINTAIN_MODE = 0x0400
    RUNNING_FORCED_MODE = 0x0800
    RUNNING_OFFGRID_MODE = 0x1000
    RESTARTING = 0x2501
    RUNNING_EXTERNAL_EMS_MODE = 0x4000


class RunningState(Flag):
    pv_power: bool
    battery_charging: bool
    battery_discharging: bool
    load_is_active: bool
    power_feed_in_the_grid: bool
    importing_power_from_grid: bool
    _reserved: None
    power_generated_from_load: bool


system_state_variable_13000 = VariableDefinition(
    VariableType.READ,
    "system_state",
    13000,
    RawType.U16,
    SystemState,
    devices=all_hybrid,
)
running_state_variable_13001 = VariableDefinition(
    VariableType.READ,
    "running_state",
    13001,
    RawType.U16,
    RunningState,
    devices=all_hybrid,
)
daily_pv_generation_variable_13002 = VariableDefinition(
    VariableType.READ,
    "daily_pv_generation",
    13002,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_pv_generation_variable_13003 = VariableDefinition(
    VariableType.READ,
    "total_pv_generation",
    13003,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
daily_export_from_pv_variable_13005 = VariableDefinition(
    VariableType.READ,
    "daily_export_from_pv",
    13005,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_export_from_pv_variable_13006 = VariableDefinition(
    VariableType.READ,
    "total_export_from_pv",
    13006,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
load_power_variable_13008 = VariableDefinition(
    VariableType.READ,
    "load_power",
    13008,
    RawType.S32,
    int,
    unit="W",
    devices=all_hybrid,
)
export_power_variable_13010 = VariableDefinition(
    VariableType.READ,
    "export_power",
    13010,
    RawType.S32,
    int,
    unit="W",
    devices=all_hybrid,
)
daily_battery_charge_energy_from_pv_variable_13012 = VariableDefinition(
    VariableType.READ,
    "daily_battery_charge_energy_from_pv",
    13012,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_battery_charge_energy_from_pv_variable_13013 = VariableDefinition(
    VariableType.READ,
    "total_battery_charge_energy_from_pv",
    13013,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
co2_reduction_variable_13015 = VariableDefinition(
    VariableType.READ,
    "co2_reduction",
    13015,
    RawType.U32,
    float,
    transform=0.1,
    unit="kg",
    devices=all_hybrid,
)
daily_direct_energy_consumption_variable_13017 = VariableDefinition(
    VariableType.READ,
    "daily_direct_energy_consumption",
    13017,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_direct_energy_consumption_variable_13018 = VariableDefinition(
    VariableType.READ,
    "total_direct_energy_consumption",
    13018,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
battery_voltage_variable_13020 = VariableDefinition(
    VariableType.READ,
    "battery_voltage",
    13020,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    devices=all_hybrid,
)
battery_current_variable_13021 = VariableDefinition(
    VariableType.READ,
    "battery_current",
    13021,
    RawType.U16,
    float,
    transform=0.1,
    unit="A",
    devices=all_hybrid,
)
battery_power_variable_13022 = VariableDefinition(
    VariableType.READ,
    "battery_power",
    13022,
    RawType.U16,
    int,
    unit="W",
    devices=all_hybrid,
)
battery_level_variable_13023 = VariableDefinition(
    VariableType.READ,
    "battery_level",
    13023,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    devices=all_hybrid,
)
battery_health_variable_13024 = VariableDefinition(
    VariableType.READ,
    "battery_health",
    13024,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    devices=all_hybrid,
)
battery_temperature_variable_13025 = VariableDefinition(
    VariableType.READ,
    "battery_temperature",
    13025,
    RawType.S16,
    float,
    transform=0.1,
    unit="°C",
    devices=all_hybrid,
)
daily_battery_discharge_energy_variable_13026 = VariableDefinition(
    VariableType.READ,
    "daily_battery_discharge_energy",
    13026,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_battery_discharge_energy_variable_13027 = VariableDefinition(
    VariableType.READ,
    "total_battery_discharge_energy",
    13027,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
daily_self_consumption_variable_13029 = VariableDefinition(
    VariableType.READ,
    "daily_self_consumption",
    13029,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    devices=all_hybrid,
)


class GridState(Enum):
    OFF_GRID = 0xAA
    ON_GRID = 0x55


grid_state_variable_13030 = VariableDefinition(
    VariableType.READ,
    "grid_state",
    13030,
    RawType.U16,
    GridState,
    transform=lambda raw: None if raw == 0xFFFF else GridState(raw),
    devices=all_hybrid,
)

phase_a_current_variable_13031 = VariableDefinition(
    VariableType.READ,
    "phase_a_current",
    13031,
    RawType.S16,
    float,
    transform=0.1,
    unit="A",
    devices=all_hybrid,
)
phase_b_current_variable_13032 = VariableDefinition(
    VariableType.READ,
    "phase_b_current",
    13032,
    RawType.S16,
    float,
    transform=0.1,
    unit="A",
    devices=all_hybrid,
    if_output_type={OutputType.THREE_PHASE_3P4L, OutputType.THREE_PHASE_3P3L},
)
phase_c_current_variable_13033 = VariableDefinition(
    VariableType.READ,
    "phase_c_current",
    13033,
    RawType.S16,
    float,
    transform=0.1,
    unit="A",
    devices=all_hybrid,
    if_output_type={OutputType.THREE_PHASE_3P4L, OutputType.THREE_PHASE_3P3L},
)

total_active_power_variable_13034 = VariableDefinition(
    VariableType.READ,
    "total_active_power",
    13034,
    RawType.S32,
    int,
    unit="W",
    devices=all_hybrid,
)
daily_import_energy_variable_13036 = VariableDefinition(
    VariableType.READ,
    "daily_import_energy",
    13036,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_import_energy_variable_13037 = VariableDefinition(
    VariableType.READ,
    "total_import_energy",
    13037,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
# note: handled by holding register 13057
# battery_capacity_variable_13039 = VariableDefinition(VariableType.READ, "battery_capacity", 13039, RawType.U16, float, transform=0.1, devices={sh5k_20, sh3k6, sh4k6, sh5k_30, sh5k_v13, sh3k6_30, sh4k6_30})
daily_charge_energy_variable_13040 = VariableDefinition(
    VariableType.READ,
    "daily_charge_energy",
    13040,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_charge_energy_variable_13041 = VariableDefinition(
    VariableType.READ,
    "total_charge_energy",
    13041,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
drm_state_variable_13043 = VariableDefinition(
    VariableType.READ, "drm_state", 13043, RawType.U16, int, devices=all_hybrid
)
daily_export_energy_variable_13045 = VariableDefinition(
    VariableType.READ,
    "daily_export_energy",
    13045,
    RawType.U16,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)
total_export_energy_variable_13046 = VariableDefinition(
    VariableType.READ,
    "total_export_energy",
    13046,
    RawType.U32,
    float,
    transform=0.1,
    unit="kWh",
    devices=all_hybrid,
)

# TODO: alarms and faults (registers 13050-13079 for hybrid)
# TODO: BMS info (registers 13100-13118 for hybrid)

start_stop_variable_13000 = VariableDefinition(
    VariableType.READWRITE,
    "start_stop",
    13000,
    RawType.U16,
    StartStop,
    devices=all_hybrid,
)
battery_maintenance_variable_13001 = VariableDefinition(
    VariableType.READWRITE,
    "battery_maintenance",
    13001,
    RawType.U16,
    bool,
    transform=(lambda raw: raw == 0xAA, lambda val: 0xAA if val else 0x55),
    devices={sh5k_20, sh3k6, sh4k6, sh5k_30, sh5k_v13, sh3k6_30, sh4k6_30},
)


class LoadAdjustmentMode(Enum):
    TIMING = 0
    ON_OFF = 1
    POWER_OPTIMIZED = 2


load_adjustment_mode_variable_13002 = VariableDefinition(
    VariableType.READWRITE,
    "load_adjustment_mode",
    13002,
    RawType.U16,
    LoadAdjustmentMode,
    transform=(
        lambda raw: None
        if not isinstance(raw, int) or raw > 2
        else LoadAdjustmentMode(raw),
        lambda val: val.value if val is not None else 3,
    ),
    devices=all_hybrid,
)
load_period_1_start_variable_13003 = VariableDefinition(
    VariableType.READWRITE,
    "load_period_1_start",
    13003,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)
load_period_1_end_variable_13005 = VariableDefinition(
    VariableType.READWRITE,
    "load_period_1_end",
    13005,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)
load_period_2_start_variable_13007 = VariableDefinition(
    VariableType.READWRITE,
    "load_period_2_start",
    13007,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)
load_period_2_end_variable_13009 = VariableDefinition(
    VariableType.READWRITE,
    "load_period_2_end",
    13009,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)


class OnOffMode(Enum):
    ON = 0xAA
    OFF = 0x55


load_on_off_mode_variable_13011 = VariableDefinition(
    VariableType.READWRITE,
    "load_on_off_mode",
    13011,
    RawType.U16,
    OnOffMode,
    devices=all_hybrid,
)
load_optimized_start_variable_13012 = VariableDefinition(
    VariableType.READWRITE,
    "load_optimized_start",
    13012,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)
load_optimized_end_variable_13014 = VariableDefinition(
    VariableType.READWRITE,
    "load_optimized_end",
    13014,
    RawType.RAW,
    time,
    length=2,
    transform=(
        lambda raw: time(raw[0], raw[1]) if isinstance(raw, tuple) else None,
        lambda val: (val.hour, val.minute),
    ),
    devices=all_hybrid,
)
load_optimized_power_variable_13016 = VariableDefinition(
    VariableType.READWRITE,
    "load_optimized_power",
    13016,
    RawType.U16,
    int,
    unit="W",
    limits=(0, 5000),
    devices=all_hybrid,
)


class EMSMode(Enum):
    SELF_CONSUMPTION = 0
    FORCED = 1
    EXTERNAL_EMS = 2


ems_mode_variable_13050 = VariableDefinition(
    VariableType.READWRITE, "ems_mode", 13050, RawType.U16, EMSMode, devices=all_hybrid
)


class ChargeDischargeCommand(Enum):
    CHARGE = 0xAA
    DISCHARGE = 0xBB
    STOP = 0xCC


charge_discharge_command_variable_13051 = VariableDefinition(
    VariableType.READWRITE,
    "charge_discharge_command",
    13051,
    RawType.U16,
    ChargeDischargeCommand,
    devices=all_hybrid,
)
charge_discharge_power_variable_13052 = VariableDefinition(
    VariableType.READWRITE,
    "charge_discharge",
    13052,
    RawType.U16,
    int,
    unit="W",
    limits=(0, 5000),
    devices=all_hybrid,
)


class BatteryType(Enum):
    LEAD_ACID_NARADA = 0
    LI_ION_SAMSUNG = 1
    NO_BATTERY = 2
    LEAD_ACID_OTHER = 3
    LI_ION_US2000A = 4
    LI_ION_LG = 5
    LI_ION_US2000B = 6
    LI_ION_GCL = 7
    LI_ION_BLUESUN = 8
    LI_ION_SUNGROW = 9
    LI_ION_BYD = 10

    @property
    def manufacturer(self) -> Optional[str]:
        """Manufacturer of the battery type, if known."""

        if self == BatteryType.LEAD_ACID_NARADA:
            return "Narada"
        elif self == BatteryType.LI_ION_BYD:
            return "BYD"
        elif self == BatteryType.LI_ION_SAMSUNG:
            return "Samsung"
        elif self == BatteryType.LI_ION_US2000A or self == BatteryType.LI_ION_US2000B:
            return "Pylontech"
        elif self == BatteryType.LI_ION_LG:
            return "LG"
        elif self == BatteryType.LI_ION_GCL:
            return "GCL"
        elif self == BatteryType.LI_ION_BLUESUN:
            return "Bluesun"
        elif self == BatteryType.LI_ION_SUNGROW:
            return "Sungrow"
        else:
            return None


battery_type_variable_13055 = VariableDefinition(
    VariableType.READWRITE,
    "battery_type",
    13055,
    RawType.U16,
    BatteryType,
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
battery_nominal_voltage_variable_13056 = VariableDefinition(
    VariableType.READWRITE,
    "battery_nominal_voltage",
    13056,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    limits=(30, 60),
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
battery_capacity_variable_13057 = VariableDefinition(
    VariableType.READWRITE,
    "battery_capacity",
    13057,
    RawType.U16,
    int,
    unit="Ah",
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
max_soc_variable_13058 = VariableDefinition(
    VariableType.READWRITE,
    "max_soc",
    13058,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    limits=(70.0, 100.0),
    devices=all_hybrid,
)
min_soc_variable_13059 = VariableDefinition(
    VariableType.READWRITE,
    "min_soc",
    13059,
    RawType.U16,
    float,
    transform=0.1,
    unit="%",
    limits=(0.0, 50.0),
    devices=all_hybrid,
)
battery_over_voltage_threshold_variable_13060 = VariableDefinition(
    VariableType.READWRITE,
    "battery_over_voltage_threshold",
    13060,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    limits=(48.0, 70.0),
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
battery_under_voltage_threshold_variable_13061 = VariableDefinition(
    VariableType.READWRITE,
    "battery_under_voltage_threshold",
    13061,
    RawType.U16,
    float,
    transform=0.1,
    unit="V",
    limits=(32.0, 48.0),
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
battery_over_temperature_threshold_variable_13062 = VariableDefinition(
    VariableType.READWRITE,
    "battery_over_temperature_threshold",
    13062,
    RawType.U16,
    float,
    transform=0.1,
    unit="°C",
    limits=(20.0, 60.0),
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
battery_under_temperature_threshold_variable_13063 = VariableDefinition(
    VariableType.READWRITE,
    "battery_under_temperature_threshold",
    13063,
    RawType.U16,
    float,
    transform=0.1,
    unit="°C",
    limits=(-30.0, 10.0),
    devices={sh5k_20, sh5k_30, sh5k_v13, sh3k6, sh3k6_30, sh4k6, sh4k6_30},
)
# TODO: battery parameters in registers 13065-13073 (hybrid)
export_power_limitation_variable_13074 = VariableDefinition(
    VariableType.READWRITE,
    "export_power_limitation",
    13074,
    RawType.U16,
    int,
    unit="W",
    devices=all_hybrid,
)
off_grid_enabled_variable_13075 = VariableDefinition(
    VariableType.READWRITE,
    "off_grid_enabled",
    13075,
    RawType.U16,
    bool,
    transform=(lambda raw: raw == 0xAA, lambda val: 0xAA if val else 0x55),
    devices=all_hybrid,
)
external_ems_heartbeat_variable_13080 = VariableDefinition(
    VariableType.READWRITE,
    "external_ems_heartbeat",
    13080,
    RawType.U16,
    int,
    unit="s",
    limits=(0, 20),
    devices=all_hybrid,
)
export_power_limitation_variable_13087 = VariableDefinition(
    VariableType.READWRITE,
    "export_power_limitation_enabled",
    13087,
    RawType.U16,
    bool,
    transform=(lambda raw: raw == 0xAA, lambda val: 0xAA if val else 0x55),
    devices={sh5_0rt, sh6_0rt, sh8_0rt, sh10rt},
)
reserved_soc_for_backup_variable_13100 = VariableDefinition(
    VariableType.READWRITE,
    "reserved_soc_for_backup",
    13100,
    RawType.U16,
    int,
    unit="%",
    limits=(0, 100),
    devices=all_hybrid,
)
