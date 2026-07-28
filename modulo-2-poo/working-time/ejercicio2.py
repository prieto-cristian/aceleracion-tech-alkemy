#######################################################################
# 2. Crear una clase llamada Animal, otra llamada Perro y otra llamada
# Águila.
# ● La clase Animal tiene:
# ○ atributo cantidad_patas: numérico
# ○ atributo tipo: vertebrado/invertebrado
# ○ metodo comer(): retorna un string “estoy comiendo”
#
# ○ La clase Perro hereda de Animal y agrega:
# ○ atributo nombre: texto
# ○ atributo raza: texto
# ○ metodo correr(): retorna un string “estoy corriendo”
#
# ○ La clase Aguila hereda de Animal y agrega:
# ○ metodo volar(): retorna un string “estoy volando”
#
# ● Guardarlo en un archivo llamado ejercicio2.py
#######################################################################

class Animal:
    def __init__(self, cantidad_patas: int, tipo: str):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        return f"Estoy comiendo"\


class Perro(Animal):
    def __init__(self, cantidad_patas: int, tipo: str, nombre: str,
                 raza: str):
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        return f"Estoy corriendo"


class Aguila(Animal):
    def __init__(self, cantidad_patas, tipo):
        super().__init__(cantidad_patas, tipo)

    def volar(self):
        return f"Estoy volando"


perro1 = Perro(4, "Vertebrado", "Fido", "Pastor aleman")
aguila1 = Aguila(2, "Vertebrado")

print(perro1.comer())
print(perro1.correr())
print(aguila1.volar())
