import copy


# Prototype interface
class Prototype:
    def clone(self):
        pass

# Concrete Prototype
class ConcretePrototype(Prototype):
    def __init__(self, value):
        self.value = value

    def clone(self):
        # Using copy module for shallow copy
        return copy.copy(self)

# Client
class Client:
    def __init__(self, prototype):
        self.prototype = prototype

    def operation(self):
        # Clone the prototype to create a new object
        cloned_object = self.prototype.clone()
        return cloned_object

# Usage
if __name__ == "__main__":
    # Create an instance of ConcretePrototype
    original_object = ConcretePrototype(value="Original Value")

    # Create a client with the prototype
    client = Client(prototype=original_object)

    # Clone the prototype to create a new object
    cloned_object = client.operation()

    # Output the values of the original and cloned objects
    print(f"Original Object Value: {original_object.value}")
    print(f"Cloned Object Value: {cloned_object.value}")
