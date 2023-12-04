# Subsystem 1
class SubsystemA:
    def operation_a1(self):
        print("SubsystemA: Operation A1")

    def operation_a2(self):
        print("SubsystemA: Operation A2")

# Subsystem 2
class SubsystemB:
    def operation_b1(self):
        print("SubsystemB: Operation B1")

    def operation_b2(self):
        print("SubsystemB: Operation B2")

# Facade
class Facade:
    def __init__(self, subsystem_a, subsystem_b):
        self._subsystem_a = subsystem_a
        self._subsystem_b = subsystem_b

    def operation(self):
        print("Facade: Operation")
        self._subsystem_a.operation_a1()
        self._subsystem_a.operation_a2()
        self._subsystem_b.operation_b1()
        self._subsystem_b.operation_b2()

# Client code
subsystem_a = SubsystemA()
subsystem_b = SubsystemB()

facade = Facade(subsystem_a, subsystem_b)
facade.operation()
