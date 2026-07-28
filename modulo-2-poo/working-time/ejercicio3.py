#######################################################################
# 3. A partir del siguiente enunciado, crear las clases necesarias
# (con sus respectivos atributos y métodos) para poder representarlos.
#
# “Juan Lopez tiene 25 años y es de profesión Abogado. Por la tarde,
# después de trabajar, sale a caminar. También tiene una bicicleta
# amarilla marca “Massino” y a veces sale a dar vueltas en ella”.
#
# ● Guardarlo en un archivo llamado ejercicio3.py
#######################################################################

class Persona:
    def __init__(self, nombre, apellido, anios: int, profesion,
                 horario_trabajo: tuple, bicicleta: Bicicleta):
        self.nombre = nombre
        self.apellido = apellido
        self.anios = anios
        self.profesion = profesion.capitalize()
        self.horario_trabajo = horario_trabajo
        self.bicicleta = bicicleta

    def esta_trabajando(self, hora_actual):
        if self.horario_trabajo[0] < hora_actual < self.horario_trabajo[1]:
            return True
        return False

    def caminar(self):
        return f"{self.nombre} se fue a caminar"

    def bicicletear(self):
        return f"{self.nombre} se fue a bicicletear en su bici {self.bicicleta}"


class Bicicleta:
    def __init__(self, color, manubrio, marca):
        self.color = color
        self.manubrio = manubrio
        self.marca = marca

    def __str__(self):
        return f"{self.marca} de color {self.color}"


# PROGRAMA DE PRUEBA
bici1 = Bicicleta("rojo", "Arco", "Olmo")
persona1 = Persona("Juan", "Lopez", 25, "Abogado", (8,17), bici1)
while True:
    hora_actual = int(input("Que hora es?"))
    if not persona1.esta_trabajando(hora_actual):
        print(f"{persona1.nombre} salio del trabajo")
        opcion = input("Quiere caminar o bicicletear?")
        match opcion:
            case "caminar":
                print(persona1.caminar())
            case "bicicletear":
                print(persona1.bicicletear())
        break
    else:
        print(f"{persona1.nombre} se encuentra trabajando. Sale a las "
              + f"{persona1.horario_trabajo[1]}")