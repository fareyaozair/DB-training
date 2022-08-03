from creditaccount import CreditAccount
from bankaccountimpl import BankAccountImpl
from insufficientfunds import InsufficientFunds
import pytest

class TestCreditAccount(object):
    def test_get_balance(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        result = subject.get_balance()

        assert result == opening_balance

    def test_debit(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        result = subject.debit(50)

        assert result == opening_balance - 50

    def test_debit_insufficient_funds(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        with pytest.raises(InsufficientFunds):
            assert subject.debit(550)

    def test_debit_negative_amount(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        with pytest.raises(Exception):
            assert subject.debit(-50)

    def test_credit(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        result = subject.credit(50)

        assert result == opening_balance + 50

    def test_credit_negative_amount(self):
        opening_balance = 500
        parent = BankAccountImpl(opening_balance)
        subject = CreditAccount(parent)

        with pytest.raises(Exception):
            assert subject.credit(-50)
