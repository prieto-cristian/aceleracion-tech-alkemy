#######################################################################
#
#######################################################################

class Vehiculo:
    def __init__(self, color : str, ruedas : int):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return (f"Informacion del vehiculo.\n\tColor: {self.color}"
                + f"\n\tRuedas: {self.ruedas}\n")

class Coche(Vehiculo):
    def __init__(self, color: str, ruedas: int, velocidad: int, patente: str):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.__patente = patente

    def obtener_patente(self):
        return self.__patente

    def actualizar_patente(self, nueva_patente):
        self.__patente = nueva_patente

    def __str__(self):
        return (f"Informacion del coche: \n\tColor: {self.color}"
                + f"\n\tRuedas: {self.ruedas}"
                + f"\n\tVelocidad: {self.velocidad}km/h "
                + f"\n\tPatente: {self.__patente}\n")


class Bicicleta(Vehiculo):
    def __init__(self, color: str, ruedas: int, tipo: str):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return (f"Informacion bicicleta:\n\tColor: {self.color}"
                + f"\n\tRuedas: {self.ruedas}\n\tTipo: {self.tipo}\n")

vehiculo = Vehiculo("verde", 5)
coche = Coche("rojo", 4, 180, "XYZ-876")
bicicleta = Bicicleta("celeste", 5, "Urbana")

print(vehiculo)
print(coche)
print(bicicleta)
coche.actualizar_patente("ABC-123")
print(coche)