class Menu:
    def __init__(self):
        self.coffee_types = {
            "espresso": {"water": 50, "milk": 0, "coffee_beans": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee_beans": 24, "cost": 2.5},
            "cappuccino": {"water": 150, "milk": 100, "coffee_beans": 24, "cost": 3.0}
        }

    def display_menu(self):
        print("\nMenu:")
        for coffee, details in self.coffee_types.items():
            print(f"{coffee.title()}: Water - {details['water']}ml, "
                  f"Milk - {details['milk']}ml, Coffee Beans - {details['coffee_beans']}g, Cost - ${details['cost']}")

    def get_coffee_details(self, coffee_choice):
        return self.coffee_types.get(coffee_choice, None)
