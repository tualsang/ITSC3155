import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    ###  write the rest of the codes ###
    while True:
        userChoice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if userChoice == "off":
            break
        elif userChoice == "report":
            for item, quantity in sandwich_maker_instance.machine_resources.items():
                print(f"{item.capitalize()}: {quantity}")
            break
        elif userChoice in ["small", "medium", "large"]:
            sandwich = recipes[userChoice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(userChoice, sandwich["ingredients"])
            else:
                print(f"Sorry not enough ingredients.")
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()
