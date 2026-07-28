from Car import Car
from Driver import Driver

class UberBlack(Car):
    def __init__(self, id: int, license_plate: str, un_conductor: Driver,
                 seats_material: str):
        super().__init__(id, license_plate, un_conductor)
        self.seats_material = seats_material

    def __str__(self):
        return super().__str__() + f"\n\tTapizado: {self.seats_material}"