from Payment import Payment

class Tarjeta(Payment):
    def __init__(self, id: int, amount: float, card_number: str, cvv: int):
        super().__init__(id, amount)
        self.card_number = card_number
        self.cvv = cvv

    def __str__(self):
        return (super().__str__() +
                f"con Tarjeta terminada en {self.card_number[-4:]}")