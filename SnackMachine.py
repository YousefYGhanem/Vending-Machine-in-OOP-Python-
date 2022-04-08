from Snack import Snack


# class for the VM
class SnackMachine:
    # setting up VM with snacks and money
    def __init__(self):
        self.snacks = []
        self.money: float = 0

    # returning the a snack by its index
    def getsnack(self, index):
        return self.snacks[index]

    # returning the current total money used in VM
    def getmoney(self):
        return self.money

    # adding a new snack to the VM
    def add_snack(self, snack: Snack):
        if len(self.snacks) <= 25:
            self.snacks.append(snack)

    # inserting money to the VM
    def add_money(self, money):
        self.money += money
        self.money = round(self.money, 2)

    # takes the input of the keypad and validates it(check if snack with selected number exists) and returns
    # the selected snack
    def validate(self, inp):
        keypad = int(inp)
        if len(self.snacks) >= keypad > 0:
            return self.snacks[keypad - 1]
        else:
            return 0

    # resets the money in the VM to use in a new purchase
    def reset(self):
        self.money = 0
