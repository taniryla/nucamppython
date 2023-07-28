from banking_pkg import account

balance = 0

print("")
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
pin = input("Enter PIN:")
print(f"{name} has been registered with a starting balance of ${balance}")

# first infinite while loops (prompt user to login)

while True:
    print("")
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_to_validate = input("Enter name:")
    pin_to_validate = input("Enter PIN:")
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful")
        break
    print("Invalid credentials!")

# second infinite while loop (prompt user to choose from atm menu


def atm_menu(name):
    while True:
        print(f"User: {name}")
        print("------------------------------------------")
        print("| 1.    Balance     | 2.    Deposit      |")
        print("------------------------------------------")
        print("------------------------------------------")
        print("| 3.    Withdraw    | 4.    Logout       |")
        print("------------------------------------------")
        option = input("Choose an option:")
        if input == "1":
            account.show_balance(balance)
        elif input == "2":
            account.deposit(balance)
            print(f"Current Balance: ${float(balance)}")
        elif input == "3":
            account.withdraw(balance)
            print(f"Current Balance: ${float(balance)}")
        else:
            account.logout(name)
            break


atm_menu(name)
