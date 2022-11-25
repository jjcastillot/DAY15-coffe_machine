from resources import MENU, resources, logo

# Main variables
master_power = 'on'

#Main display
print("COFFEE MACHINE 3000")
print(logo)
print("Current resources:")
print(f"Water: {resources['water']}\nMilk: {resources['milk']}")
print(f"Coffee: {resources['coffee']}")
choice = input('''
What would you like today?
A) Espresso
B) Latte
C) Capuccino 
''').lower()

if choice == 'off':
    print("MACHINE TURNED OFF")
    pass
else:
    print('bye')
