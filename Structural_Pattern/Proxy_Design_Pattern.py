# Subject interface
class RealSubject:
    def request(self):
        print("RealSubject: Handling request")

# Proxy class
class Proxy:
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # Perform some additional operations before delegating to the real subject
        print("Proxy: Logging the request")
        self._real_subject.request()
        print("Proxy: Post-processing the request")

# Client code
real_subject = RealSubject()
proxy = Proxy(real_subject)

# Client interacts with the proxy, which in turn interacts with the real subject
proxy.request()
