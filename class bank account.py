class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0  # Initial balance set to zero

    # Method to deposit an amount to the balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    # Method to withdraw an amount from the balance if there are sufficient funds
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    # Method to apply interest to the current balance
    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f"Applied interest. New balance is {self.balance}.")

    # Method to display account holder's name and current balance
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")

# Example usage
account1 = BankAccount("John Doe")

# Display initial account info
account1.display_account_info()

# Deposit some money
account1.deposit(500)

# Withdraw some money
account1.withdraw(200)

# Apply interest
account1.apply_interest()

# Display updated account info
account1.display_account_info()
