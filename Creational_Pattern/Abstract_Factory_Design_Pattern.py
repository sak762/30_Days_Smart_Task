from abc import ABC, abstractmethod


# Abstract Products
class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass

# Concrete Products
class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Product A1 operation"

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Product A2 operation"

class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Product B1 operation"

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Product B2 operation"

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

# Concrete Factories
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()

# Client
class Client:
    def __init__(self, factory):
        self.product_a = factory.create_product_a()
        self.product_b = factory.create_product_b()

    def operate(self):
        result_a = self.product_a.operation_a()
        result_b = self.product_b.operation_b()
        return f"{result_a} and {result_b}"

# Usage
if __name__ == "__main__":
    # Using Factory 1
    factory_1 = ConcreteFactory1()
    client_1 = Client(factory_1)
    result_1 = client_1.operate()
    print(result_1)

    # Using Factory 2
    factory_2 = ConcreteFactory2()
    client_2 = Client(factory_2)
    result_2 = client_2.operate()
    print(result_2)
