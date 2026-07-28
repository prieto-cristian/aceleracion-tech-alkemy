from Payment import Payment

class Efectivo(Payment):
    def __init__(self, id, amount):
        super().__init__(id, amount)

    def __str__(self):
        return super().__str__() + "en Efectivo."