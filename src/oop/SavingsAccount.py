from src.oop.BankAccount import BankAccount


class SavingsAccount(BankAccount):

    def __init__(self, owner, interest_rate = 0.05, balance = 0):
        super().__init__(owner, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        self._balance += self._balance * self.interest_rate
