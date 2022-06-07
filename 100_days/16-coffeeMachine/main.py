from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



new_menu = Menu()

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

acumulated_money = 0

def enough_resources(order_ingredients):
    enough_items = True
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            enough_items = False
    return enough_items

def process_coins():
    print('Please, insert coins')
    quarters = int(input('How many quarters?:'))
    dimes = int(input('How many dimes?:'))
    nickles = int(input('How many nickles?:'))
    pennies = int(input('How many pennies?:'))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

def counting_coins(money_inserted, drink_cost):
    global acumulated_money 
    successful = False
    if money_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return
    if money_inserted > drink_cost:
        print(f"Here is ${money_inserted - drink_cost} dollars in change.")
    acumulated_money += drink_cost
    print(acumulated_money)
    successful = True
    return successful





while True:
    user_answer = input(f'What would you like? {new_menu.get_items()}:\n')
    if user_answer == 'off':
        break
    if user_answer == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${acumulated_money}")
        continue
    new_choice = new_menu.find_drink(user_answer)
    first_verification = enough_resources(new_choice.ingredients)
    if first_verification:
        second_verification = counting_coins(process_coins(), new_choice.cost)

    if first_verification and second_verification:
        for ingredient in new_choice.ingredients:
            resources[ingredient] -= new_choice.ingredients[ingredient]
        print(f'Here is your {user_answer}. Enjoy!')
