from Driver import Driver

class Car:
    def __init__(self, id, license_plate, un_conductor: Driver):
        self.id = id
        self.license_plate = license_plate
        self.conductor = un_conductor

    def __str__(self):
        return (f"\n\t\tPatente: {self.license_plate}, "
                + f"\n\t\tConductor: {self.conductor}")