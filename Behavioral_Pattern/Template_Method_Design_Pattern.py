from abc import ABC, abstractmethod


# Abstract class with the template method
class AbstractClassTemplate(ABC):
    def template_method(self):
        self.common_operation1()
        self.different_operation()
        self.common_operation2()

    @abstractmethod
    def different_operation(self):
        pass

    def common_operation1(self):
        print("Common Operation 1")

    def common_operation2(self):
        print("Common Operation 2")

# Concrete class implementing the template method
class ConcreteClass1(AbstractClassTemplate):
    def different_operation(self):
        print("Customized Operation for ConcreteClass1")

# Concrete class implementing the template method
class ConcreteClass2(AbstractClassTemplate):
    def different_operation(self):
        print("Customized Operation for ConcreteClass2")

# Client code
if __name__ == "__main__":
    # Client uses the template method with ConcreteClass1
    instance1 = ConcreteClass1()
    instance1.template_method()

    print("------------------------")

    # Client uses the template method with ConcreteClass2
    instance2 = ConcreteClass2()
    instance2.template_method()
