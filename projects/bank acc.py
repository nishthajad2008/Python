class BankAccount:
    def __init__(self,owner: str,balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self,amount):
        if amount <= 0:
            print("Invalid deposit amount")
        else:
            self.balance += amount
            return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
            return self.balance
        else:
            self.balance -= amount
            return self.balance
if __name__ == "__main__":
    acc = BankAccount("Alice", 100.0)

    print(acc.deposit(50.0))
    print(acc.withdraw(30.0))
    print(acc.withdraw(200.0))
    print(acc.deposit(-10.0))