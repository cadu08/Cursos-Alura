class Account:

    def __init__(self, number, holder, balance, limit):
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def statement(self):
        print("Balance of holder {}: US${}".format(self.holder, self.balance))

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
