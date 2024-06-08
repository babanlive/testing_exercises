import datetime
import pytest

from functions.level_1.two_date_parser import compose_datetime_from


# Пробую использовать fixture для тестов
@pytest.fixture(autouse=True)
def setup_test_data(request):
    request.cls.today = datetime.date.today()
    request.cls.tomorrow = request.cls.today + datetime.timedelta(days=1)
    request.cls.time_str = "12:30"
    request.cls.wrong_time_str = "26:30"


class TestTwoDateParser:
    def test_compose_datetime_from(self):
        assert compose_datetime_from("anytime", self.time_str) == datetime.datetime(
            self.today.year, self.today.month, self.today.day, 12, 30
        )
        assert compose_datetime_from("tomorrow", self.time_str) == datetime.datetime(
            self.tomorrow.year, self.tomorrow.month, self.tomorrow.day, 12, 30
        )
        with pytest.raises(ValueError):
            compose_datetime_from("tomorrow", self.wrong_time_str)
