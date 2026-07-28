class Animal:
    especie = "Mamifero"

    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

perro1 = Animal("Milo", "Salchicha")
print(f"Nombre: {perro1.nombre} - Raza: {perro1.raza}")
print(Animal.especie)
print(type(perro1))

# Que hace vars? Buscar
print(vars(perro1))

# Que hace dir? Buscar
print(dir(perro1))