# from tkinter import Menu

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

def enough_resources(drink):
    enough_items = True
    for ingredient in MENU[drink]['ingredients']:
        if MENU[drink]['ingredients'][ingredient] > resources[ingredient]:
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

def counting_coins(money_inserted, drink):
    global acumulated_money 
    successful = False
    if money_inserted < MENU[drink]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return
    if money_inserted > MENU[drink]['cost']:
        print(f"Here is ${money_inserted - MENU[drink]['cost']} dollars in change.")
    acumulated_money += MENU[drink]['cost']
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
    
    first_verification = enough_resources(user_answer)
    # money = process_coins()
    second_verification = counting_coins(process_coins(), user_answer)

    if first_verification and second_verification:
        for ingredient in MENU[user_answer]['ingredients']:
            resources[ingredient] -= MENU[user_answer]['ingredients'][ingredient]
        print(f'Here is your {user_answer}. Enjoy!')
