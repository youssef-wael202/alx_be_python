class BankAccount:
    def __init__(self,initial_balance=0):
        self.initial_balance =initial_balance
    def deposit(self,amount):
        self.account_balance += amount
    def withdraw(self,amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"your current balance: ${self.account_balance}")