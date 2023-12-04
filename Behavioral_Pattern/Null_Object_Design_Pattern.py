# Abstract class/interface
class AbstractCustomer:
    def is_null(self):
        pass

    def get_name(self):
        pass

# Concrete class - Real Customer
class RealCustomer(AbstractCustomer):
    def __init__(self, name):
        self.name = name

    def is_null(self):
        return False

    def get_name(self):
        return self.name

# Concrete class - Null Customer
class NullCustomer(AbstractCustomer):
    def is_null(self):
        return True

    def get_name(self):
        return "Not Available"

# CustomerFactory to create Real or Null Customer
class CustomerFactory:
    customers = [RealCustomer("Joe"), RealCustomer("Alice"), RealCustomer("Bob")]

    @classmethod
    def get_customer(cls, name):
        for customer in cls.customers:
            if customer.get_name() == name:
                return customer
        return NullCustomer()

# Usage
if __name__ == "__main__":
    customer_factory = CustomerFactory()

    customer1 = customer_factory.get_customer("Joe")
    customer2 = customer_factory.get_customer("Alice")
    customer3 = customer_factory.get_customer("Bob")
    customer4 = customer_factory.get_customer("Charlie")

    print("Customers:")
    print(customer1.get_name())  # Output: Joe
    print(customer2.get_name())  # Output: Alice
    print(customer3.get_name())  # Output: Bob
    print(customer4.get_name())  # Output: Not Available
