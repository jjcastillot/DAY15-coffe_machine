from resources import MENU, resources, logo

# Main variables
master_power = 'on'
keep_working = True
profit = 0

# Functions
def check_resources(menu_choice,available_resources):
    '''Checks if are available resources to prepare the drink'''
    water = available_resources['water'] - menu_choice['water']
    milk = available_resources['milk'] - menu_choice['milk']
    coffee = available_resources['coffee'] - menu_choice['coffee']

    if (water < 0) or (milk < 0) or (coffee < 0): return False
    else: return True

def print_resources():
    print("Current resources:")
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Profits: ${profit}")

def resources_updater(menu_choice):
    resources['water'] -= menu_choice['water']
    resources['milk'] -= menu_choice['milk']
    resources['coffee'] -= menu_choice['coffee']

#Main display
print("COFFEE MACHINE 3000")
print(logo)
print_resources()
while (master_power == 'on') and (keep_working ==True):
    choice = input('''
What would you like today?
Espresso
Latte
Cappuccino 
    ''').lower()

    if choice == 'off':
        print("MACHINE TURNED OFF")
        master_power = 'off'
    elif choice == 'report':
        print_resources()
    elif (choice == 'espresso') or (choice == 'latte') or (choice == 'cappuccino'):
        available = check_resources(MENU[choice]['ingredients'],resources)
        if available:
            print(f"OK, it costs ${MENU[choice]['cost']}, please insert your coins:")
            quarters = int(input("Quarters: "))
            dimes = int(input("Dimes: "))
            nickels = int(input("Nickels: "))
            pennies = int(input("Pennies: "))
            money = 0.25*quarters + 0.1*dimes + 0.05*nickels + 0.01*pennies
            if money >= MENU[choice]['cost']:
                change = money - MENU[choice]['cost']
                profit += money - change
                print(f"Here is ${round(change,2)} in change.")
                resources_updater(MENU[choice]['ingredients'])
                #print_resources()
                print(f"Here's your {choice}, enjoy!")
            else:
                print(f"Sorry, you need ${MENU[choice]['cost'] - money} more for that drink. MONEY REFUNDED")



        else:
            print("Sorry, there are not enough resources for this")

    else: print("Sorry, NOT AVAILABLE INSTRUCTION")

    if master_power == 'on':
        another_drink = input("Do you want another drink? (Y/N): ").lower()
        if another_drink == 'y':
            keep_working = True
        else:
            keep_working = False