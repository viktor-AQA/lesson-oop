class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        try:
            if amount > 0:
                self._balance += amount
        except ValueError:
            print("пополнение не может быть отрицацельным")

    def withdraw(self, amount):
        try:
            if self._balance >= amount:
                self._balance -= amount
        except ValueError:
            print("На балансе недостаточно средств")

    def get_balance(self):
        print(f"Баланс: {self._balance}")
        return self._balance
