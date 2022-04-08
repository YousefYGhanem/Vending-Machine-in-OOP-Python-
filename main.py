import random

from CardSlot import CardSlot
from CoinSlot import CoinSlot
from Money import Money
from NotesSlot import NotesSlot
from Snack import Snack
from SnackMachine import SnackMachine

# VM object
machine = SnackMachine()

# global variables
curr_snack: Snack
money: Money


# check if number (string) is a float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


# initializing the VM and adding snacks to it
def initialise():
    snack_names = ["Ghirardelli", "Kit Kat", "Cheez-It", "Cheetos", "Kellogg's", "Campbell's", "Nestlé Toll House",
                   "Dove", "Quaker", "Tostitos", "Snickers", "Cheerios", "Fritos", "Pringles", "Lay's Chips",
                   "Betty Crocker", "Jif", "Planters", "Doritos", "Ritz", "Pillsbury", "Oreo Cookies", "Reese's",
                   "Hershey's", "M&M's"]
    for i in range(0, 25):
        machine.add_snack(Snack(name=snack_names[i], number=i + 1, cost=round(random.uniform(0.1, 10), 1)))


# the start of the process and the main view
def start():
    global curr_snack
    machine.reset()
    print("\n")
    print("-" * 200)
    c = 0

    # viewing the available snacks
    for i in range(0, 5):
        for j in range(0, 5):
            print("{ Product:" + machine.getsnack(c).getname() + ", Number:" + str(machine.getsnack(c).getnumber()) +
                  " }\t||\t", end="")
            c += 1
        print()

    print("-" * 200 + "\n")

    # selecting a snack by number and validate it
    curr_snack = machine.validate(input("Please enter the snack number: "))
    if curr_snack == 0:
        input('The number you entered is not valid!\nPlease press enter to continue...')
        print("\n")
        start()

    print("snack number is valid.")
    print("You selected the following snack: " + str(curr_snack))
    ui_pay()


# goes to the view of payment selection
def ui_pay():
    # asking the user for the payment method
    print("\nHow would you like to pay?\n1 - Coins (Machine only accepts [10c, 20c, 50c and 1$])\n"
          "2 - Notes (Machine only accepts [20$ and 50$])\n3 - Credit Card\n4 - Previous")
    inp = input("Answer: ")
    print()
    match inp:
        case '1':
            pay_by_coin()
        case '2':
            pay_by_note()
        case '3':
            pay_by_card()
        case '4':
            start()
        case _:
            print("Answer is not valid!!")
            ui_pay()


# payment by credit card process
def pay_by_card():
    # entering a fake balance for the card
    inp = input("Please enter a fake balance for your credit card (in $) : ")
    if isfloat(inp):
        card = CardSlot(float(inp))
        print("\nYour current balance is: " + str(card.getbalance()) + "$")

        # checking if the card balance can purchase the selected snack
        if card.buy(curr_snack.getcost()) == 0:
            print("Your current balance is not enough to purchase this item.")
            input("Please press enter to continue...")
            start()
        else:
            print("Purchasing snack...")
            print("Purchase completed\n\nYour current balance is: " + str(card.getbalance()) + "$")
            print("The machine is dispensing " + curr_snack.getname() + " for you!")
            input("Please press enter to take the snack...")
            print("\nHave a nice day ^-^")
            input("\n\nPlease press enter to buy again...")
            start()
    else:
        print("This isn't a valid number!")
        pay_by_card()


# payment by notes
def pay_by_note():
    global money

    # checking the total money in the VM is enough for the purchase
    if machine.getmoney() >= curr_snack.getcost():
        accept()

    # using the Notes slot object
    money = NotesSlot()

    # inserting notes
    inp = input("Please insert Notes (only 20$ and 50$) (enter 0 to stop): ")
    if inp == "0":
        print("The current amount is not enough for the purchase!\nThe machine is returning it now.")
        input("Please press enter to take the money...")
        start()

    print("\nverifying...\n")
    # verifying if the note is usable (if yes adding it to the total)
    if money.set_coin(inp) == 0:
        print("Invalid input!")
    else:
        machine.add_money(money.getvalue())
        print("You inserted " + money.gettype())
        print("Total: " + str(machine.getmoney()) + "$\n")
    pay_by_note()


# payment by coins
def pay_by_coin():
    global money

    # checking the total money in the VM is enough for the purchase
    if machine.getmoney() >= curr_snack.getcost():
        accept()
    money = CoinSlot()
    # inserting coins
    inp = input("Please insert coins (only 10c, 20c, 50c, 1$) (enter 0 to stop): ")
    if inp == "0":
        print("The current amount is not enough for the purchase!\nThe machine is returning it now.")
        input("Please press enter to take the money...")
        start()

    print("\nverifying...\n")
    # verifying if the coin is usable (if yes adding it to the total)
    if money.set_coin(inp) == 0:
        print("Invalid input!")
    else:
        machine.add_money(money.getvalue())
        print("You inserted " + money.gettype())
        print("Total: " + str(machine.getmoney()) + "$\n")
    pay_by_coin()


# reporting to user that the money is accepted and dispensing the snack, returning change if needed
def accept():
    print("Money accepted!")
    print("The machine is dispensing " + curr_snack.getname() + " for you!")
    input("Please press enter to take the snack...")
    if machine.getmoney() > curr_snack.getcost():
        change = machine.getmoney() - curr_snack.getcost()
        change = round(change, 2)
        print("Your change is: " + str(change) + "$")
        input("Please press enter to take it...")
    print("\nHave a nice day ^-^")
    input("\n\nPlease press enter to buy again...")

    # getting back to the main view
    start()


# The main function
if __name__ == "__main__":
    initialise()
    start()
