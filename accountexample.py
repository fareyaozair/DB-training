from creditaccount import CreditAccount
from bankaccountimpl import BankAccountImpl


if __name__ == '__main__':    
    bankAcc = BankAccountImpl(30.00)
    print(bankAcc.getBalance())

    creditAcc = CreditAccount(bankAcc)
    bal = creditAcc.get_balance()
    print(bal)

    creditAcc.credit(150)
    print(creditAcc.get_balance())

    creditAcc.debit(70)
    print(creditAcc.get_balance())

