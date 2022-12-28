from typing import List

from pysungrow.definitions.device import SungrowDevice

from . import hybrid, string

devices: List[SungrowDevice] = [
    v
    for module in [hybrid, string]
    for v in module.__dict__.values()
    if isinstance(v, SungrowDevice)
]
