from BankAccount import BankAccount

def test_initial_balance():
    account = BankAccount("Антон", 100)
    assert account.get_balance() == 100.0

def test_deposit_balance():
    account = BankAccount("Антон", 100)
    account.deposit(50)
    assert account.get_balance() == 150.0

def test_withdraw_balance():
    account = BankAccount("Антон", 100)
    account.withdraw(30)
    assert account.get_balance() == 70.0

def test_withdraw_more_balance():
    account = BankAccount("Антон", 100)
    account.withdraw(150)
    assert account.get_balance() == 100.0  # Balance should remain the same

def test_negative_deposit():
    account = BankAccount("Антон", 100)
    account.deposit(-50)
    assert account.get_balance() == 100.0  # Balance should remain the same

def test_balance_is_positive():
    account = BankAccount("Антон", 100)
    assert account.get_balance() > 0  # Check that balance is greater than 0