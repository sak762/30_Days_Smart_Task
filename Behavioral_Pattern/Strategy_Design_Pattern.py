from abc import ABC, abstractmethod


# Define the strategy interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} via Credit Card")

# Concrete strategy 2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying {amount} via PayPal")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self._payment_strategy = payment_strategy

    def checkout(self, amount):
        self._payment_strategy.pay(amount)

# Client code
if __name__ == "__main__":
    # Client chooses a payment strategy
    credit_card_strategy = CreditCardPayment()
    paypal_strategy = PayPalPayment()

    # Client creates a context with a specific strategy
    cart1 = ShoppingCart(credit_card_strategy)
    cart2 = ShoppingCart(paypal_strategy)

    # Client uses the context to perform an action (checkout)
    cart1.checkout(100)
    cart2.checkout(50)
