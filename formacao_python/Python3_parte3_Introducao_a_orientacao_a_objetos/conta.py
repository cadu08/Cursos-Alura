class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building an object ... {}".format(self))
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
