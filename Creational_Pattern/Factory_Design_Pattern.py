from abc import ABC, abstractmethod


# Abstract Product
class Product(ABC):
    @abstractmethod
    def create(self):
        pass

# Concrete Products
class ConcreteProductA(Product):
    def create(self):
        return "Product A"

class ConcreteProductB(Product):
    def create(self):
        return "Product B"

# Abstract Factory
class Factory(ABC):
    @abstractmethod
    def create_product(self):
        pass

# Concrete Factories
class ConcreteFactoryA(Factory):
    def create_product(self):
        return ConcreteProductA()

class ConcreteFactoryB(Factory):
    def create_product(self):
        return ConcreteProductB()

# Client
class Client:
    def __init__(self, factory):
        self.factory = factory

    def produce(self):
        product = self.factory.create_product()
        return product.create()

# Usage
if __name__ == "__main__":
    # Using Factory A
    factory_a = ConcreteFactoryA()
    client_a = Client(factory_a)
    result_a = client_a.produce()
    print(result_a)  # Output: Product A

    # Using Factory B
    factory_b = ConcreteFactoryB()
    client_b = Client(factory_b)
    result_b = client_b.produce()
    print(result_b)  # Output: Product B
