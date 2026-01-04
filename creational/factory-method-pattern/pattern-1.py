from abc import ABC, abstractmethod

# 1) ------------ Product (Interface / Abstract Class)--------------------

class PaymentGatewayInterface(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# 2) --------------- Concrete Product --------------------------------------

class PayPalPaymentGateway(PaymentGatewayInterface):
    def process_payment(self, amount):
        return f" Processing $ {amount} through paypal pg"

class RazorPayPaymentGateway(PaymentGatewayInterface):
    def process_payment(self, amount):
        return f" Processing $ {amount} through razorpay pg"


# 3) --------------- Define the Factory (Creator) ------------------------
# the factory decides which pg to create

class PaymentFactory(ABC):
    @abstractmethod
    def create_pg(self):
        pass

    def make_payment(self, amount):
        gateway = self.create_pg()
        return gateway.process_payment(amount)

# 4) Concrete factories

class PayPalFactory(PaymentFactory):
    def create_pg(self):
        return PayPalPaymentGateway()

    def make_payment(self, amount):
        return self.create_pg().process_payment(amount)

class RazorPayFactory(PaymentFactory):
    def create_pg(self):
        return RazorPayPaymentGateway()

    def make_payment(self, amount):
        return self.create_pg().process_payment(amount)

# step 5) Client code


if __name__ == '__main__':

    payment_type = input("enter a payment gateway type (paypal, razorpay) : ")
    amount = 1000
    factory = None

    if payment_type == "paypal":
        factory = PayPalFactory()
    elif payment_type == "razorpay":
        factory = RazorPayFactory()
    else:
        raise ValueError("enter a valid payment gateway")

    print(factory.make_payment(amount))
