import string

from Money import Money


# child of class (Money) for Coins slot
class CoinSlot(Money):
    def __init__(self):
        self.type: string = None
        self.value: float = 0

    def gettype(self):
        return self.type

    def getvalue(self):
        return self.value

    def set_coin(self, payment: string):
        if payment == "10c":
            self.type = payment
            self.value = 0.1
        elif payment == "20c":
            self.type = payment
            self.value = 0.2
        elif payment == "50c":
            self.type = payment
            self.value = 0.5
        elif payment == "1$":
            self.type = payment
            self.value = 1
        else:
            return 0
        return 1
