class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # in ml
        self.milk = 500  # in ml
        self.coffee_beans = 200  # in grams
        self.money = 0  # in dollars

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

    def check_resources(self, coffee_choice):
        required = self.coffee_types[coffee_choice]
        if self.water < required['water']:
            print("Sorry, not enough water!")
            return False
        if self.milk < required['milk']:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < required['coffee_beans']:
            print("Sorry, not enough coffee beans!")
            return False
        return True

    def make_coffee(self, coffee_choice):
        required = self.coffee_types[coffee_choice]
        self.water -= required['water']
        self.milk -= required['milk']
        self.coffee_beans -= required['coffee_beans']
        self.money += required['cost']
        print(f"Here is your {coffee_choice}, enjoy!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Which coffee would you like? (espresso/latte/cappuccino): ").lower()
            if choice in self.coffee_types:
                if self.check_resources(choice):
                    print(f"Making your {choice}...")
                    self.make_coffee(choice)
            else:
                print("Invalid choice. Please choose a valid coffee type.")

            # Simple way to exit the loop
            if input("Would you like another coffee? (yes/no): ").lower() != "yes":
                print("Thank you for using the Coffee Machine. Have a great day!")
                break

# Create and run the coffee machine
coffee_machine = CoffeeMachine()
coffee_machine.run()


