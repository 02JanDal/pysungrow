from pysungrow.definitions.devices.hybrid import sh10rt
from pysungrow.definitions.variables.device import _get_sungrow_device


def test_get_sungrow_device():
    assert _get_sungrow_device(0xE03) == sh10rt
