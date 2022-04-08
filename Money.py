from abc import ABC, abstractmethod


# Abstract class for Money types
class Money(ABC):
    @abstractmethod
    # abstract function for returning value and currency of the money
    def gettype(self):
        pass

    @abstractmethod
    # abstract function for returning value of the money
    def getvalue(self):
        pass

    @abstractmethod
    # validating inserted money and setting it in the object
    def set_coin(self, payment):
        pass
