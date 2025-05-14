from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine =  CoffeeMaker()
drinks = Menu()
registrator = MoneyMachine()

isOn = True
while isOn:
    menu = drinks.get_items()
    order = input(f"Select your drink: {menu}\n")
    if order == "report":
        print(machine.report())
    elif order == "off":
        isOn = False
    else:
        coffee = drinks.find_drink(order)
        if  machine.is_resource_sufficient(coffee):
            if registrator.make_payment(coffee.cost):
                machine.make_coffee(coffee)
        else:
            print("Not enough resources.")



