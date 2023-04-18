# Encapsulating --> Methods and Attributes
# Data Abstraction
# Inheritance
# Polymorphism

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return self.owner + " : " + str(self.balance)
    
    def inquire(self):
        print("Balance: ", self.balance)

class SavingsAccount(Account):
    def __init__(self, rate, owner, balance):
        super().__init__(owner, balance)
        self.rate = rate

    def display_rate(self):
        print(self.rate)

    def inquire(self):
        print("Savings Balance: ", self.balance)


my_account = Account("Ahsan", 5000)

savings_account = SavingsAccount(15.0, "Ali", 2000)

my_account.inquire()
savings_account.inquire()