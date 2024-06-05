import pytest

from functions.level_1.five_title import change_copy_item

@pytest.mark.parametrize(
    "title, max_main_item_title_length, expected",
    [
        ('Title', 100, 'Copy of Title'),
        ('Title', 10, 'Title'),
        ('Copy of Title', 100, 'Copy of Title (2)'),
        ('Copy of Title (2)', 100, 'Copy of Title (3)'),
        ('Copy of Title(1)' , 100, 'Copy of (2)'),
    ]
)
def test_change_copy_item(title, max_main_item_title_length, expected):
    assert change_copy_item(title, max_main_item_title_length) == expected
