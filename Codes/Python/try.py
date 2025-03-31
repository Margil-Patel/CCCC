class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn. Remaining balance: ₹{self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} added for {self.name}")

    def get_accounts(self):
        return self.accounts


class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added to {self.name}")

    def get_customers(self):
        return self.customers


# Example Usage
if __name__ == "__main__":
    bank = Bank("State Bank")
    
    # Creating customers
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")

    # Adding customers to the bank
    bank.add_customer(customer1)
    bank.add_customer(customer2)

    # Creating accounts
    account1 = BankAccount("A001", 1000)
    account2 = BankAccount("A002", 500)

    # Assigning accounts to customers
    customer1.add_account(account1)
    customer2.add_account(account2)

    # Performing transactions
    account1.deposit(500)
    account1.withdraw(300)
    print(f"Alice's final balance: ₹{account1.get_balance()}")

    account2.deposit(1000)
    account2.withdraw(700)
    print(f"Bob's final balance: ₹{account2.get_balance()}")

