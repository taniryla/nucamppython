from app import balance


def show_balance(balance):
    print(f"Your balance is {float(balance)}")


def deposit(balance):
    str_amount = input("Enter amount to deposit:")
    amount = int(str_amount)
    current_balance = amount + balance
    return current_balance


def withdraw(balance):
    str_withdraw = input("Enter amount to withdraw:")
    withdraw = int(str_withdraw)
    current_balance = balance - withdraw
    return current_balance


def logout(name):
    print(f"Goodbye {name}")


current_balance = balance
