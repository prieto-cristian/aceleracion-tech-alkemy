class Route:
    def __init__(self, start: str, end: str):
        self.ruta = (start, end)

    def __str__(self):
        return f"Sale de {self.ruta[0]} con destino a {self.ruta[1]}"