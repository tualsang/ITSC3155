class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, quantity in ingredients.items():
            if quantity > self.machine_resources[item]:
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, quantity in order_ingredients.items():
            self.machine_resources[item] -= quantity
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
