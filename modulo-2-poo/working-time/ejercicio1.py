#######################################################################
# 1. Crear una clase llamada Bicicleta y luego aplica los siguientes
# accionables:
# ○ Agregar al menos 3 atributos
# ○ Agregar al menos 3 métodos
# ○ Agregar el metodo constructor de la clase.
# ● Guardarlo en un archivo llamado ejercicio1.py
#######################################################################
class Bicicleta:
    def __init__(self, color, manubrio, marca):
        self.color = color
        self.manubrio = manubrio
        self.marca = marca

    def obtener_marca(self):
        return self.marca

    def actualizar_manubrio(self, nuevo_manubrio):
        self.manubrio = nuevo_manubrio

    def pintar(self, nuevo_color):
        self.color = nuevo_color

    def __str__(self):
        return (f"INFORMACION BICICLETA:\n\tMarca: {self.marca}\n\tColor:"
                + f"{self.color}\n\tManubrio: {self.manubrio}")


bici1 = Bicicleta("azul", "recto", "Olmo")
print(bici1)