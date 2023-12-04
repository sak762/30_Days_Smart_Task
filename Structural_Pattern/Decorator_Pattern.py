# Component interface
class Coffee:
    def cost(self):
        pass

# Concrete component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete decorator
class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return super().cost() + 2

# Another concrete decorator
class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def cost(self):
        return super().cost() + 1

# Client code
simple_coffee = SimpleCoffee()
print(f"Cost of simple coffee: ${simple_coffee.cost()}")

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost of milk coffee: ${milk_coffee.cost()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost of sugar milk coffee: ${sugar_milk_coffee.cost()}")
