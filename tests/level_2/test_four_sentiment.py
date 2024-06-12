import pytest

from functions.level_2.four_sentiment import check_tweet_sentiment


@pytest.mark.parametrize(
    "text, good_words, bad_words, expected",
    [
        ("this is test text", {"good"}, {"bad"}, None),
        ("this is bad test text", {"good"}, {"bad"}, "BAD"),
        ("this is good test text", {"good"}, {"bad"}, "GOOD"),
        ("this is good test text bad", {"good"}, {"bad"}, None),
        ("this is good bad bad test text", {"good"}, {"bad"}, "BAD"),
        ("this is good bad good test text", {"good"}, {"bad"}, "GOOD"),
    ],
)
def test__check_tweet_sentiment(text, good_words, bad_words, expected):
    assert check_tweet_sentiment(text, good_words, bad_words) == expected


def test__check_tweet_sentiment__text_is_int():
    with pytest.raises(AttributeError):
        check_tweet_sentiment(123, {"good"}, {"bad"})


def test__check_tweet_sentiment__good_words_is_int():
    with pytest.raises(TypeError):
        check_tweet_sentiment("text", 123, {"bad"})
