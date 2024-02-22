from resources import Resources
from menu import Menu

class CoffeeMachine:
    def __init__(self):
        self.resources = Resources()
        self.menu = Menu()

    def make_coffee(self, coffee_choice):
        coffee = self.menu.get_coffee_details(coffee_choice)
        if coffee and self.check_resources(coffee):
            self.process_coffee(coffee)
            print(f"Here is your {coffee_choice}, enjoy!")

    def check_resources(self, coffee):
        if self.resources.water < coffee['water']:
            print("Sorry, not enough water!")
            return False
        if self.resources.milk < coffee['milk']:
            print("Sorry, not enough milk!")
            return False
        if self.resources.coffee_beans < coffee['coffee_beans']:
            print("Sorry, not enough coffee beans!")
            return False
        return True

    def process_coffee(self, coffee):
        self.resources.water -= coffee['water']
        self.resources.milk -= coffee['milk']
        self.resources.coffee_beans -= coffee['coffee_beans']
        self.resources.money += coffee['cost']

def main():
    machine = CoffeeMachine()
    while True:
        machine.menu.display_menu()
        choice = input("Which coffee would you like? (espresso/latte/cappuccino): ").lower()
        if choice in machine.menu.coffee_types:
            machine.make_coffee(choice)
        else:
            print("Invalid choice. Please choose a valid coffee type.")

        if input("Would you like another coffee? (yes/no): ").lower() != "yes":
            print("Thank you for using the Coffee Machine. Have a great day!")
            break

if __name__ == "__main__":
    main()
