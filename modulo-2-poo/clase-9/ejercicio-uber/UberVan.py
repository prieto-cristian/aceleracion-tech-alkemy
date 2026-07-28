from Car import Car
from Driver import Driver

class UberVan(Car):
    def __init__(self, id: int, license_plate: str, un_conductor: Driver,
                 capacity: int):
        super().__init__(id, license_plate, un_conductor)
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f", Capacidad: {self.capacity}"