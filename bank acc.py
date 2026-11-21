class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("\n---> Account Details <---")
        print("Account Number:", self.acc_no)
        print("Name:", self.name)
        print("Account Type:", self.acc_type)
        print("Balance:", self.balance)


# Getting account details from user
acc_no = int(input("Enter account number: "))
name = input("Enter account holder name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating object
acc = BankAccount(acc_no, name, acc_type, balance)

# Deposit
deposit_amount = float(input("\nEnter deposit amount: "))
acc.deposit(deposit_amount)

# Withdrawal
withdraw_amount = float(input("Enter withdrawal amount: "))
acc.withdraw(withdraw_amount)

# Display final details
acc.display()
