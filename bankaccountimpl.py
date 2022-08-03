from account import Account


class BankAccountImpl(Account):

    def __init__(self, balance):
        self.itsBalance = balance
        #add properties etc.

    def get_balance(self):
        return self.itsBalance
    
    def debit(self, amount):
        self.itsBalance -= amount
        return self.itsBalance
    
    def credit(self, amount):
        self.itsBalance += amount
        return self.itsBalance

