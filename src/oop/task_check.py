from src.oop.SavingsAccount import SavingsAccount

example_user = SavingsAccount("Антон", interest_rate = 0.05)
example_user.deposit(500)
example_user.withdraw(100)
example_user.apply_interest()
example_user.get_balance()
