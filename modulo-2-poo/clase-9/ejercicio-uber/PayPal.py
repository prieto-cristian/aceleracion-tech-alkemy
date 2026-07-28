from Payment import Payment

class PayPal(Payment):
    def __init__(self, id, amount,paypal_email):
        super().__init__(id, amount)
        self.paypal_email = paypal_email

    def __str__(self):
        return super().__str__() + f"con PayPal ({self.paypal_email})"