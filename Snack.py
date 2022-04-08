import string


# class for a snack in the VM
class Snack:
    # setting up the snack by its name, cost, and number in the VM
    def __init__(self, name: string, number: int, cost: float):
        self.name = name
        self.number = number
        self.cost = cost

    # for printing a snack
    def __repr__(self):
        return "name:% s | number:% d | cost:%.1f$" % (self.name, self.number, self.cost)

    # return the name of the snack
    def getname(self):
        return self.name

    # return the number of the snack
    def getnumber(self):
        return self.number

    # return the cost of the snack
    def getcost(self):
        return self.cost
