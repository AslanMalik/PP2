class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"Balance: {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("Not enough money")
        else:
            self.balance -= money
        print(f"Balance: {self.balance}")


owner = input()
balance = int(input())

account = Account(owner, balance)

account.deposit(100)    
account.withdraw(50)     
account.withdraw(200) 

