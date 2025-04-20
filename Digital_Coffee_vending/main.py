#TODO 1. Check resources sufficient to make the drink

from menu import MENU
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False  
    return True  
def process_coins():
    """Returns the total calculated from coins inserted."""

    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25 
    total += int(input("How many dimes? ")) * 0.10 
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01 
    return total
    
def is_transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    

    
is_on = True
while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
#TODO 2. Turning  off the coffee machine
    if choice == "off":
        is_on = False

#TODO 3. Print report of resources
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
       
