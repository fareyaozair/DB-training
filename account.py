from abc import ABC, abstractmethod


class Account(ABC):

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def debit(self, amount):
        pass

    @abstractmethod
    def credit(self, amount):
        pass

