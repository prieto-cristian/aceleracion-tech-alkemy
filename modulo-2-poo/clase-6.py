##############################################################################
# EJERCICIO PRACTICO EN CLASE: POO
# Objetivo: Crear tu primera clase en Python
#
# 1. Crea una clase llamada "Mascota" con los atributos:
#   . nombre (str)
#   . especie (str)
#   . energia (int) -> Debe iniciar siempre en 100
#
# 2. Define el metodo jugar():
#   . Resta 20 puntos de energia
#   . Muestra un mensaje en pantalla (ej: Fido esta jugando)
#
# 3. Define el metodo comer():
#   . Suma 15 puntos de energia.
#   . Muestra un mensaje en pantalla
#
# 4. Prueba tu codigo:
#   . Crea 2 instancias (ej: un perro y un gato)
#   . Haz que jueguen, coman y muestra su energia final por consola
##############################################################################

class Mascota:
    def __init__(self, nombre, especie):
        self.nombre = nombre.capitalize()
        self.especie = especie
        self.energia = 100

    def jugar(self):
        if self.energia >= 20:
            self.energia -= 20
            print(f"{self.nombre} jugado esta jugando! -20 de energia.")
        else:
            print(f"{self.nombre} no tiene energia para jugar.")

    def comer(self):
        if self.energia <= 85:
            self.energia += 15
            print(f"{self.nombre} esta comiendo! +15 de energia.")
        else:
            print(f"{self.nombre} no tiene hambre.")

perro = Mascota("Rocky", "Perro")
gato = Mascota("Michi", "Gato")
perro.jugar()
perro.jugar()
perro.jugar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.jugar()
perro.comer()
perro.comer()
gato.comer()
print("FIN DEL DIA")
print(f"{perro.nombre} tiene {perro.energia} de energia.")
print(f"{gato.nombre} tiene {gato.energia} de energia.")