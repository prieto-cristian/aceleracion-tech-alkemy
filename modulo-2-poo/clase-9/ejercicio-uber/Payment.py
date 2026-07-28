class Payment:
    def __init__(self, id, amount):
        self.id = id
        self.amount = amount

    def __str__(self):
        return f"${self.amount:.2f} pesos "