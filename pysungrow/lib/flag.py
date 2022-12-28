"""Provides the Flag class."""

from typing import Dict, List


class Flag:
    """A class to handle bitfield-style ints representing several flags."""

    def __init__(self, value: int):
        """
        Construct an instance of this flag class, including parsing bits into the defined flags.

        :param value: Bitfield-like integer to extract bits from
        """
        # __annotations__ assumed to be ordered: https://stackoverflow.com/a/64446226
        for index, entry in enumerate(self.__annotations__.keys()):
            if entry.startswith("_"):
                continue
            self.__dict__[entry] = bool(value & (1 << index))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(f'{e}={self.__dict__[e]}' for e in self.keys())})"

    def keys(self) -> List[str]:
        """Return the keys of the flags handled by this class."""
        return [k for k in self.__annotations__.keys() if not k.startswith("_")]

    def to_dict(self) -> Dict[str, bool]:
        """Return the flags with their values in this class."""
        return {k: self.__dict__[k] for k in self.keys()}
