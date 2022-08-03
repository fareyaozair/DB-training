from insufficientfunds import InsufficientFunds


class CreditAccount:
    def __init__(self, account):
        self.itsParent = account

    def get_balance(self):
        return self.itsParent.get_balance()
 
    def debit(self, amt):
        bal = self.itsParent.get_balance()
        if bal - amt < 0:
            raise InsufficientFunds(str(bal) + " - " + str(amt) + " cannot be completed...")

        self.itsParent.debit(amt)
        
        return self.itsParent.get_balance()
    
    def credit(self, amt):
        self.itsParent.credit(amt)
        
        return self.itsParent.get_balance()
