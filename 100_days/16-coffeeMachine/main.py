from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_menu = Menu()
new_coffeemaker = CoffeeMaker()
new_moneymachine = MoneyMachine()

while True:
    user_answer = input(f'What would you like? {new_menu.get_items()}:\n')
    if user_answer == 'off':
        break
    if user_answer == 'report':
        new_coffeemaker.report()
        new_moneymachine.report()
        continue
    
    new_choice = new_menu.find_drink(user_answer)
    
    if new_coffeemaker.is_resource_sufficient(new_choice):
        if new_moneymachine.make_payment(new_choice.cost):
            new_coffeemaker.make_coffee(new_choice)

