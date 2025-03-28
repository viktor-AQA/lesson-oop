from src.oop.BankAccount import BankAccount


class CheckingAccount(BankAccount):

        def __init__(self, owner, balance=0):
            super().__init__(owner, balance)

        def withdraw(self, amount):
            self._balance -= amount
