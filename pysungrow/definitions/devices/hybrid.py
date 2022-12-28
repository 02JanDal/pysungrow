from pysungrow.definitions.device import SungrowDevice, SungrowDeviceType

sh5k_20 = SungrowDevice(0xD09, "SH5K-20", SungrowDeviceType.HYBRID)
sh3k6 = SungrowDevice(
    0xD06,
    "SH3K6",
    SungrowDeviceType.HYBRID,
)
sh4k6 = SungrowDevice(
    0xD07,
    "SH4K6",
    SungrowDeviceType.HYBRID,
)
sh5k_v13 = SungrowDevice(
    0xD03,
    "SH5K-V13",
    SungrowDeviceType.HYBRID,
)
sh5k_30 = SungrowDevice(
    0xD0C,
    "SH5K-30",
    SungrowDeviceType.HYBRID,
)
sh3k6_30 = SungrowDevice(
    0xD0A,
    "SH3K6-30",
    SungrowDeviceType.HYBRID,
)
sh4k6_30 = SungrowDevice(
    0xD0B,
    "SH4K6-30",
    SungrowDeviceType.HYBRID,
)
sh5_0rs = SungrowDevice(
    0xD0F,
    "SH5.0RS",
    SungrowDeviceType.HYBRID,
)
sh3_6rs = SungrowDevice(
    0xD0D,
    "SH3.6RS",
    SungrowDeviceType.HYBRID,
)
sh4_6rs = SungrowDevice(
    0xD0E,
    "SH4.6RS",
    SungrowDeviceType.HYBRID,
)
sh6_0rs = SungrowDevice(
    0xD10,
    "SH6.0RS",
    SungrowDeviceType.HYBRID,
)
sh10rt = SungrowDevice(
    0xE03,
    "SH10RT",
    SungrowDeviceType.HYBRID,
)
sh8_0rt = SungrowDevice(
    0xE02,
    "SH8.0RT",
    SungrowDeviceType.HYBRID,
)
sh6_0rt = SungrowDevice(
    0xE01,
    "SH6.0RT",
    SungrowDeviceType.HYBRID,
)
sh5_0rt = SungrowDevice(
    0xE00,
    "SH5.0RT",
    SungrowDeviceType.HYBRID,
)

all_hybrid = {
    sh5k_20,
    sh3k6,
    sh4k6,
    sh5k_v13,
    sh5k_30,
    sh3k6_30,
    sh4k6_30,
    sh5_0rs,
    sh3_6rs,
    sh4_6rs,
    sh6_0rs,
    sh10rt,
    sh8_0rt,
    sh6_0rt,
    sh5_0rt,
}
