water = 300
milk = 200
coffee = 100
money = 0
espresso = {
    "price": 0,
    "water": 50,
    "coffee": 18
}
latte = {
    "price": 2.5,
    "water": 200,
    "coffee": 20,
    "milk": 150
}
cappucino = {
    "price": 2.5,
    "water": 250,
    "coffee": 24,
    "milk": 100
}

def not_enough(resource):
    """Prints out a warning of not enough resources for the particular order"""
    if resource == "water":
        print("Sorry there is not enough water.")
    elif resource == "milk":
        print("Sorry there is not enough milk")
    elif resource == "coffee":
        print("Sorry there is not enough coffee")

def check_resources(order):
    """Checks available resources (water, coffee, milk) for the given order"""
    if order.lower().strip() == "latte":
        if latte["water"]  > water:
            not_enough("water")
            return False
        elif latte["coffee"] > coffee:
            not_enough("coffee")
            return False
        elif latte["milk"] > milk:
            not_enough("milk")
            return False
    elif order.lower().strip() == "cappucino":
        if cappucino["water"]  > water:
            not_enough("water")
            return False
        elif cappucino["coffee"] > coffee:
            not_enough("coffee")
            return False
        elif cappucino["milk"] > milk:
            not_enough("milk")
            return False
    elif order.lower().strip() == "espresso":
        if espresso["water"]  > water:
            not_enough("water")
            return False
        elif espresso["coffee"] > coffee:
            not_enough("coffee")
            return False

def handle_coins(order):
    """This method sums up the input coins, checks if it can afford the order, adds it to the
    treasury (money variable), and returns the change if it was over the required fee for the order"""
    price = order["price"]
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    coin_sum = (pennies * 0.01) + (dimes * 0.1) + (nickles * 0.05) + (quarters * 0.25)
    if coin_sum < order["price"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    elif coin_sum == price:
        return price
    else:
        change = coin_sum - price
        print(f"Here is ${change} in change.")
        return price

return_action = True

while return_action:
    user_input = input("What would you like? (espresso/latte/cappucino): ").lower().strip()
    if user_input == "report":
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
    elif user_input == "off":
        return_action = False
    else:
        if check_resources(user_input) == False:
            return_action = False
        else:
            if user_input == "latte":
                result = handle_coins(latte)
                if result != 0:
                    money += result
                    print(f"Here is your {user_input}, enjoy!")
            elif user_input == "espresso":
                result = handle_coins(espresso)
                if result != 0:
                    money += result
                    print(f"Here is your {user_input}, enjoy!")
            elif user_input == "cappucino":
                result = handle_coins(cappucino)
                if result != 0:
                    money += result
                    print(f"Here is your {user_input}, enjoy!")
