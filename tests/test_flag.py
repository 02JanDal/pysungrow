from pysungrow.lib.flag import Flag


class FlagTest(Flag):
    foo: bool
    _reserved: None
    bar: bool


def test_keys():
    assert FlagTest(0).keys() == ["foo", "bar"]


def test_parses():
    assert not FlagTest(0b000).foo
    assert not FlagTest(0b000).bar
    assert not FlagTest(0b100).foo
    assert FlagTest(0b100).bar
    assert FlagTest(0b101).foo
    assert FlagTest(0b101).bar


def test_to_dict():
    assert FlagTest(0b000).to_dict() == dict(foo=False, bar=False)
    assert FlagTest(0b100).to_dict() == dict(foo=False, bar=True)


def test_repr():
    assert repr(FlagTest(0b100)) == "FlagTest(foo=False, bar=True)"
