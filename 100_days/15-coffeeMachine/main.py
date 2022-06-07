# from tkinter import Menu
from prettytable import PrettyTable


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

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
    user_answer = input('What would you like? (espresso/latte/cappuccino):\n')
    if user_answer == 'off':
        break
    if user_answer == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${acumulated_money}")
        continue
    
    first_verification = enough_resources(MENU[user_answer]['ingredients'])
    if first_verification:
        second_verification = counting_coins(process_coins(), MENU[user_answer]['cost'])

    if first_verification and second_verification:
        for ingredient in MENU[user_answer]['ingredients']:
            resources[ingredient] -= MENU[user_answer]['ingredients'][ingredient]
        print(f'Here is your {user_answer}. Enjoy!')
