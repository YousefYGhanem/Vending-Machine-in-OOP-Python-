import string
from abc import ABC

from Money import Money


# child of class (Money) for Notes slot
class NotesSlot(Money, ABC):
    def __init__(self):
        self.type: string = None
        self.value: float = 0

    def gettype(self):
        return self.type

    def getvalue(self):
        return self.value

    def set_coin(self, payment: string):
        if payment == "20$":
            self.type = payment
            self.value = 20
        elif payment == "50$":
            self.type = payment
            self.value = 50
        else:
            return 0
        return 1
