class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"


def main():
    account = BankAccount("Aya", 100)
    account.deposit(50)
    account.withdraw(30)
    print(account)


if __name__ == "__main__":
    main()
