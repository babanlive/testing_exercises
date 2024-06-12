import pytest
from functions.level_2.three_first import first


@pytest.mark.parametrize(
    "items, default, expected",
    [
        ([1, 2, 3], 4, 1),
        ([1, 2, 3], None, 1),
        ([1, 2, 3], "abc", 1),
        ([], "abc", "abc"),
        ([], None, None),
        ([], 0, 0),
    ],
)
def test__first(items, default, expected):
    assert first(items, default) == expected


def test__first__error():
    with pytest.raises(AttributeError):
        first([])
