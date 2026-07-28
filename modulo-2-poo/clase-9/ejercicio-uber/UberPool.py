from Car import Car
from Driver import Driver

class UberPool(Car):
    def __init__(self, id: int, license_plate: str, un_conductor: Driver,
                 brand: str, model: str):
        super().__init__(id, license_plate, un_conductor)
        self.brand = brand
        self.model = model

    def __str__(self):
        return (super().__str__()
                + f"\n\tMarca: {self.brand}\n\tModelo: {self.model}")