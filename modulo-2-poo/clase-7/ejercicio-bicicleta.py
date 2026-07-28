##############################################################################
# Consigna:
#
# Crear una clase llamada Bicicleta:
# - agregar el metodo init
# - agregar al menos 3 atributos
# - agregar al menos 3 metodo
##############################################################################

# Bicicleta en una bicicleteria

class Bicicleta:
    def __init__(self, color, tipo, rodado, precio, marca):
        self.__color = color
        self.__tipo = tipo
        self.__rodado = rodado
        self.__precio = precio
        self.__marca = marca.capitalize()

    def obtener_rodado(self):
        return self.__rodado

    def obtener_precio(self):
        return self.__precio

    def pintar(self, nuevo_color):
        self.__color = nuevo_color
        print(f"Modificacion de color: Bicleta {self.__marca} {self.__tipo} "
              + "ahora es de color " + nuevo_color)

    def actualizar_precio(self, nuevo_precio):
        self.__precio = nuevo_precio
        print(f"Modifiacion de precio: Bicicleta {self.__marca} {self.__tipo}"
              + " ahora vale " + str(nuevo_precio))

    def mostrar_informacion(self):
        print(f"""INFORMACION BICICLETA:
    Marca: {self.__marca}
    Color: {self.__color}
    Tipo: {self.__tipo}
    Precio: {self.__precio}
    Rodado: {self.__rodado} \n""")

bicicleta1 = Bicicleta("rojo", "Pista", 28, 357000, "Olmo")
bicicleta2 = Bicicleta("azul", "Montaña", 30, 450650, "Trek")

bicicleta1.mostrar_informacion()
bicicleta2.mostrar_informacion()

bicicleta1.pintar("verde")
bicicleta2.actualizar_precio(268090)
print("\n")
bicicleta1.mostrar_informacion()
bicicleta2.mostrar_informacion()