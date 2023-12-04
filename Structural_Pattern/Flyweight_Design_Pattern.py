# Flyweight interface
class CoffeeOrder:
    def serve_coffee(self, context):
        pass

# Concrete Flyweight
class CoffeeFlavor(CoffeeOrder):
    def __init__(self, flavor):
        self._flavor = flavor

    def serve_coffee(self, context):
        print(f"Serving coffee flavor '{self._flavor}' to table {context}")

# Flyweight Factory
class CoffeeOrderContext:
    def __init__(self):
        self._orders = {}

    def get_coffee_order(self, flavor):
        if flavor not in self._orders:
            self._orders[flavor] = CoffeeFlavor(flavor)
        return self._orders[flavor]

# Client code
table_orders = [
    ("Caramel", 1),
    ("Vanilla", 2),
    ("Caramel", 3),
    ("Espresso", 4),
    ("Vanilla", 5),
]

coffee_context = CoffeeOrderContext()

for flavor, table in table_orders:
    coffee_flavor = coffee_context.get_coffee_order(flavor)
    coffee_flavor.serve_coffee(table)
