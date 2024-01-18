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
profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffee_machine_on = True
while(coffee_machine_on):
    user_response = input("What would you like? (espresso/latte/cappuccino): ")
    if(user_response == "report"):
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g\nMoney: {profit}\n")
        continue

    elif(user_response == "espresso"):
        if(resources["water"] < MENU["espresso"]["ingredients"]["water"]):
            print("Sorry, there is not enough water.")
        elif(resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]):
            print("Sorry, there is not enough coffee.")
        else:
            print("Please insert coins.")
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickles = input("How many nickles?: ")
            pennies = input("How many pennies?: ")
            total_amount_inserted = ( float(quarters) * .25) + (float(dimes) * .1) + (float(nickles) * .05) + (float(pennies) * .01)

            if(total_amount_inserted < MENU["espresso"]["cost"]):
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                change = round(total_amount_inserted - MENU['espresso']['cost'], 2)
                profit = MENU["espresso"]["cost"]
                print(f"Here is ${change} in change.")
                print("Here is your espresso ☕ Enjoy!")


    elif(user_response == "latte"):
        if(resources["water"] < MENU["latte"]["ingredients"]["water"]):
            print("Sorry, there is not enough water.")
        elif(resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]):
            print("Sorry, there is not enough coffee.")
        elif(resources["milk"] < MENU["latte"]["ingredients"]["milk"]):
            print("Sorry, there is not enough milk.")
        else:
            print("Please insert coins.")
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickles = input("How many nickles?: ")
            pennies = input("How many pennies?: ")
            total_amount_inserted = ( float(quarters) * .25) + (float(dimes) * .1) + (float(nickles) * .05) + (float(pennies) * .01)

            if(total_amount_inserted < MENU["latte"]["cost"]):
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                change = round(total_amount_inserted - MENU['latte']['cost'], 2)
                profit = MENU["latte"]["cost"]
                print(f"Here is ${change} in change.")
                print("Here is your latte ☕ Enjoy!")

    elif(user_response == "cappuccino"):
        if(resources["water"] < MENU["cappuccino"]["ingredients"]["water"]):
            print("Sorry, there is not enough water.")
        elif(resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]):
            print("Sorry, there is not enough coffee.")
        elif(resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]):
            print("Sorry, there is not enough milk.")
        else:
            print("Please insert coins.")
            quarters = input("How many quarters?: ")
            dimes = input("How many dimes?: ")
            nickles = input("How many nickles?: ")
            pennies = input("How many pennies?: ")
            total_amount_inserted = ( float(quarters) * .25) + (float(dimes) * .1) + (float(nickles) * .05) + (float(pennies) * .01)

            if(total_amount_inserted < MENU["cappuccino"]["cost"]):
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                change = round(total_amount_inserted - MENU['cappuccino']['cost'], 2)
                profit = MENU["cappuccino"]["cost"]
                print(f"Here is ${change} in change.")
                print("Here is your cappuccino ☕ Enjoy!")

    elif(user_response == 'off'):
        coffee_machine_on = False