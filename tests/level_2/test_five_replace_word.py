import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected",
    [
        ("this is test text", "test", "test123", "this is test123 text"),
        ("this is test text", "test123", "test", "this is test text"),
        ("this is test text", "test123", "test123", "this is test text"),
    ],
)
def test__replace_word(text, replace_from, replace_to, expected):
    assert replace_word(text, replace_from, replace_to) == expected


def test__replace_word__replace_from_is_int():
    with pytest.raises(AttributeError):
        replace_word("text", 123, "test")


def test__replace_word__text_is_int():
    with pytest.raises(AttributeError):
        replace_word(123, "test", "test123")
