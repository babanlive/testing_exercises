import datetime
import decimal
import pytest

from functions.level_1.four_bank_parser import (
    BankCard,
    SmsMessage,
    Expense,
    parse_ineco_expense,
)


# пробую @pytest.mark.parametrize
@pytest.mark.parametrize(
    "sms, cards, expected",
    [
        (
            SmsMessage(
                text="999.99 RUB, 1234567887654321 04.06.24 09:32 ABComp authcode 12345",
                author="MockBank",
                sent_at=datetime.datetime.now(),
            ),
            [
                BankCard(last_digits="4321", owner="Vasya"),
            ],
            Expense(
                amount=decimal.Decimal("999.99"),
                card=BankCard(last_digits="4321", owner="Vasya"),
                spent_in="ABComp",
                spent_at=datetime.datetime(2024, 6, 4, 9, 32),
            ),
        )
    ],
)
def test_parse_ineco_expense(sms, cards, expected):
    assert parse_ineco_expense(sms, cards) == expected

# P.S. Голова закипела пока понял, что распарсить должна функция.
