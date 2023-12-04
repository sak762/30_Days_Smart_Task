# Target interface
class Target:
    def request(self):
        pass

# Adaptee (the class to be adapted)
class Adaptee:
    def specific_request(self):
        print("Adaptee: Specific request")

# Adapter (implements Target interface and contains an instance of Adaptee)
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        print("Adapter: Request")
        self._adaptee.specific_request()

# Client code
target = Target()
adaptee = Adaptee()
adapter = Adapter(adaptee)

# The client interacts with the Target interface, but the Adapter internally uses the Adaptee
target.request()
adapter.request()
