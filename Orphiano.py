# Importing necessary tools
import random  # 'import' used
from typing import List  # 'from' and 'import' used

# Creating a special error when there is not enough money
class NotEnoughMoney(Exception):  
    pass  # 'pass' means nothing happens here, just defining the error

# Creating a Bank Account class
class BankAccount:
    interest_rate = 0.05  # Interest rate for all accounts

    def __init__(self, name, balance=0):
        assert balance >= 0, "Balance cannot be negative"  # 'assert' makes sure balance is valid
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Take money out, but only if there is enough"""
        if amount > self.balance:
            raise NotEnoughMoney("Not enough money!")  # 'raise' gives an error if balance is too low
        self.balance -= amount
        return True

    def __del__(self):
        """Deletes an account when not needed"""
        print(f"{self.name}'s account is deleted.")  # 'del' used

# Function to find an account
def find_account(accounts, name):
    for account in accounts:  # 'for' and 'in' used
        if account.name == name:
            return account
    return None  # Returns 'None' if account is not found

# Function for the banking system
def main():
    global accounts  # 'global' used to access the list of accounts
    accounts = []  # List of all accounts

    while True:  # 'while' loop runs forever until user exits
        try:  # 'try' starts error handling
            print("\nSimple Bank System")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View All Accounts")
            print("5. Exit")
            
            choice = int(input("Choose an option: "))

            if choice == 1:  # 'if' used
                name = input("Enter your name: ")
                balance = float(input("Enter starting balance: "))
                if balance < 0:
                    print("Balance cannot be negative.")
                    continue  # 'continue' used to skip rest of loop if balance is invalid
                new_account = BankAccount(name, balance)
                accounts.append(new_account)
                print(f"Account created for {name}.")

            elif choice == 2:  # 'elif' used
                name = input("Enter your name: ")
                account = find_account(accounts, name)
                if account is not None:  # 'is' and 'not' used
                    amount = float(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Deposit amount must be positive.")
                        continue  # 'continue' used to restart loop if input is invalid
                    account.deposit(amount)
                    print(f"{amount} added to {name}'s account.")
                else:
                    print("Account not found.")

            elif choice == 3:
                name = input("Enter your name: ")
                account = find_account(accounts, name)
                if account:
                    try:
                        amount = float(input("Enter amount to withdraw: "))
                        if amount <= 0:
                            print("Withdrawal amount must be positive.")
                            continue  # 'continue' used to restart loop if input is invalid
                        account.withdraw(amount)
                        print(f"{amount} withdrawn from {name}'s account.")
                    except NotEnoughMoney as e:  # 'except' used
                        print(e)
                else:
                    print("Account not found.")

            elif choice == 4:
                if not accounts:
                    print("No accounts found.")
                else:
                    print("All Accounts:")
                    for account in accounts:
                        print(f"- {account.name}: ${account.balance}")

            elif choice == 5:
                print("Goodbye!")
                break  # 'break' stops the loop and exits

            else:
                print("Invalid choice. Try again.")

        except ValueError:  # Handles cases where the user enters wrong input
            print("Please enter a number.")

        finally:
            print("Transaction complete.\n")  # 'finally' always runs

# A simple interest calculator using lambda
calculate_interest = lambda balance: balance * BankAccount.interest_rate  # 'lambda' used

# A function using 'nonlocal'
def outer_function():
    message = "Hello"

    def inner_function():
        nonlocal message  # 'nonlocal' lets us change 'message' from outside
        message += ", welcome to our bank!"
        return message

    return inner_function()

# Using 'with' to handle a file safely
with open("bank_log.txt", "w") as file:  # 'with' ensures proper file handling
    file.write("Banking system started.\n")

# Generator function to yield account balances
def yield_balances(accounts):
    """Generator function to yield account balances"""
    for account in accounts:
        if account.balance > 0 and account.balance % 2 == 0:  # 'and' used
            yield account.balance  # 'yield' used

# Running the program
if __name__ == "__main__": 
    print(outer_function())  # Prints welcome message
    main()
