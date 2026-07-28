# Existen 3 tipos de metodos

class Colectivo:
    precio_pasaje = 115

    def __init__(self, numero_colectivo):
        self.numero_colectivo = numero_colectivo

    # 1. Metodo de instancia (se coloca self, siempre)
    def obtener_nro_colectivo(self):
        return self.numero_colectivo

    # 2. Metodo de clase
    @staticmethod
    def mostrar_precio():
        return precio_pasaje

    def __str__(self):
        return f"Nombre: {self.numero_colectivo}"