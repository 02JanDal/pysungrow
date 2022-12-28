from pysungrow.definitions.device import SungrowDevice, SungrowDeviceType

# based on "Communication Protocol of PV Grid-Connected String Inverters" v1.1.2 dated 2017-5-13

sg60ktl = SungrowDevice(0x10F, "SG60KTL", SungrowDeviceType.STRING)
sg60ku = SungrowDevice(0x136, "SG60KU", SungrowDeviceType.STRING)
sg33ktl_m = SungrowDevice(0x134, "SG33KTL-M", SungrowDeviceType.STRING)
sg36ktl_m = SungrowDevice(0x74, "SG36KTL-M", SungrowDeviceType.STRING)
sg40ktl_m = SungrowDevice(0x135, "SG40KTL-M", SungrowDeviceType.STRING)
sg50ktl_m = SungrowDevice(0x11B, "SG50KTL-M", SungrowDeviceType.STRING)
sg60ktl_m = SungrowDevice(0x131, "SG60KTL-M", SungrowDeviceType.STRING)
sg60ku_m = SungrowDevice(0x132, "SG60KU-M", SungrowDeviceType.STRING)
sg49k5j = SungrowDevice(0x137, "SG49K5J", SungrowDeviceType.STRING)
sg8ktl_m = SungrowDevice(0x13F, "SG8KTL-M", SungrowDeviceType.STRING)
sg10ktl_m = SungrowDevice(0x13E, "SG10KTL-M", SungrowDeviceType.STRING)
sg12ktl_m = SungrowDevice(0x13C, "SG12KTL-M", SungrowDeviceType.STRING)
sg80ktl = SungrowDevice(0x138, "SG80KTL", SungrowDeviceType.STRING)
sg80ktl_m = SungrowDevice(0x139, "SG80KTL-M", SungrowDeviceType.STRING)
sg80hv = SungrowDevice(0x13A, "SG80HV", SungrowDeviceType.STRING)
sg125hv = SungrowDevice(0x13B, "SG125HV", SungrowDeviceType.STRING)

all_string = {
    sg10ktl_m,
    sg12ktl_m,
    sg125hv,
    sg33ktl_m,
    sg36ktl_m,
    sg40ktl_m,
    sg49k5j,
    sg50ktl_m,
    sg60ktl,
    sg60ktl_m,
    sg60ku,
    sg80hv,
    sg80ktl,
    sg80ktl_m,
    sg8ktl_m,
}
