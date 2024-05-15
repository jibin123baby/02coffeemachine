
"""
This Program represents a Coffee wending Machine.
It can make 3 Varieties of coffees.
It needs money to give coffee. If money is less, it will return completely return the money.
Otherwise, it will return the change and the Selected coffee.
If input 'report' is provided, it will status report of the resources and profits.
If it doesn't have enough resources, it will suggest some alternatives.

"""
import datafile
from datafile import resources, MENU


def check_resources(user_input):
    """
        This function will check, if there is enough resources to make a coffee
    :param user_input: Type of coffee Selected by the User
                        1. Espresso
                        2. Late
                        3. Cappuccino

                        report will generate the report
                        off will turn off the machine
    :return: Whether the resources available or not
    """

    if MENU[user_input]["ingredients"]["water"] >= resources["water"]:
        print("Sorry there is not enough water.")
        return False

    elif MENU[user_input]["ingredients"]["milk"] >= resources["milk"]:
        print("Sorry there is not enough milk.")
        return False

    elif MENU[user_input]["ingredients"]["coffee"] >= resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def process_coins():
    """
        This is function will ask the user to Provide the money
        for the Coffee and calculate the Total.
    :return: The Total Money given by the User
    """
    pennies = int(input("Enter number of Pennies: "))
    nickel = int(input("Enter number of Nickels: "))
    dimes = int(input("Enter number of Dimes: "))
    quarters = int(input("Enter number of Quarters: "))

    return (pennies * 0.01) + (nickel * 0.05) + (dimes * 0.1) + (quarters * 0.25)


def update_report(user_input):
    """
        This Function will take the User Input and Update the Report
    :param user_input: User Chosen Coffee
    """
    datafile.resources["water"] -= user_input["ingredients"]["water"]
    datafile.resources["milk"] -= user_input["ingredients"]["milk"]
    datafile.resources["coffee"] -= user_input["ingredients"]["coffee"]
    datafile.profit += user_input["cost"]


def generate_report():
    """
        This function will display the details and remaining Resources
    """
    print(f"Water {datafile.resources["water"]}")
    print(f"Milk {datafile.resources["milk"]}")
    print(f"Coffee {datafile.resources["coffee"]}")
    print(f"Total Profit {datafile.profit}")


def run_coffee_machine(user_input):
    """
        This is Main Function.
        Starting Point of the Program
    :return: None
    """

    if user_input == '1':
        user_input = 'espresso'
    elif user_input == '2':
        user_input = 'latte'
    elif user_input == '3':
        user_input = 'cappuccino'

    if user_input == 'report':
        generate_report()
        return
    elif check_resources(user_input):
        print("Please Insert Coins")
        total_money = process_coins()
        print(total_money)
        if total_money >= MENU[user_input]["cost"]:
            balance = round(total_money - MENU[user_input]["cost"], 2)
            print(f"Here is ${balance} dollars in change.")
            update_report(MENU[user_input])
            print(f"Enjoy your {user_input.title()}")
        else:
            print("Sorry that\'s not enough money. Money refunded.")


isRunning = True
while isRunning:

    user_choice = (input("Please Select an Option"
                         "\n1. Espresso\n2. Latte \n3. Cappuccino\n")).lower()
    if user_choice == 'off':
        isRunning = False
    else:
        run_coffee_machine(user_choice)
    print("----------------------------------------------")
