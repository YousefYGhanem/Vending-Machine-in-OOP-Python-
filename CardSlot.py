# class for paying with a credit card
class CardSlot:
    def __init__(self, balance: float):
        self.balance = balance

    # returning the current balance of credit card
    def getbalance(self):
        return self.balance

    # used for purchasing and returning a new balance
    def buy(self, money):
        if self.balance >= money:
            self.balance -= money
            self.balance = round(self.balance, 2)
            return 1
        else:
            return 0
