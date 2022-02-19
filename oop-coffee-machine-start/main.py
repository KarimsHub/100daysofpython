from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

running = True

while running:
    options = new_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        running = False
    elif choice == "report":
        coffee_maker.report() #report method automatically prints the resources
        money_machine.report() #report method automatically prints the amount of money
    else:
        user_choice = new_menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(user_choice) and money_machine.make_payment(user_choice.cost):
            coffee_maker.make_coffee(user_choice)
