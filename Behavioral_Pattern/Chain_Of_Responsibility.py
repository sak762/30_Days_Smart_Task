# Handler interface
class Handler:
    def handle_request(self, request):
        pass

    def set_successor(self, successor):
        pass

# ConcreteHandler1
class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "Type1":
            print("ConcreteHandler1 is handling Type1 request.")
        elif self.successor:
            self.successor.handle_request(request)

    def set_successor(self, successor):
        self.successor = successor

# ConcreteHandler2
class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "Type2":
            print("ConcreteHandler2 is handling Type2 request.")
        elif self.successor:
            self.successor.handle_request(request)

    def set_successor(self, successor):
        self.successor = successor

# Client
class Client:
    def __init__(self):
        self.handler_chain = ConcreteHandler1()
        handler2 = ConcreteHandler2()
        self.handler_chain.set_successor(handler2)

    def send_request(self, request):
        self.handler_chain.handle_request(request)

# Usage
client = Client()
client.send_request("Type1")  # Output: ConcreteHandler1 is handling Type1 request.
client.send_request("Type2")  # Output: ConcreteHandler2 is handling Type2 request.
client.send_request("Type3")  # Output: (No handler can handle Type3 request)
