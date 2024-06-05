from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url("example.com", "relative_url") == "example.com/relative_url"
    assert build_url("example.com", "relative_url", {"key": "value"}) == "example.com/relative_url?key=value"
    assert build_url("example.com", "relative_url", {"key1": "value1", "key2": "value2"}) == "example.com/relative_url?key1=value1&key2=value2"
    assert build_url("example.com", "relative_url", None) == "example.com/relative_url"