from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize("Работал", "Работала", "male") == "Работал"
    assert genderalize("Работал", "Работала", "female") == "Работала"
    assert genderalize("Работал", "Работала", "unknown") == "Работала"
    assert not genderalize("Работал", "Работала", "unknown") == "Работал"
