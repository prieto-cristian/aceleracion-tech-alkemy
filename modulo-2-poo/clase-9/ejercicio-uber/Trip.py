from User import User
from Car import Car
from Route import Route
from Payment import Payment

class Trip:
    def __init__(self, trip_id: int, user: User, car: Car, route: Route,
                 payment: Payment):
        if not isinstance(trip_id, int):
            print("ID debe ser un entero")
        elif not isinstance(user, User):
            print("El usuario no es valido")
        elif not isinstance(car, Car):
            print("El vehiculo ingresado no es valido")
        elif not isinstance(route, Route):
            print("La ruta ingresada no es valida")
        elif not isinstance(payment, Payment):
            print("El metodo de pago no es valido")
        else:
            self.trip_id = trip_id
            self.user = user
            self.car = car
            self.route = route
            self.payment = payment

    def summary(self):
        print(f"INFORMACION DEL VIAJE:\n\tNumero viaje: {self.trip_id}"
              + f"\n\tUSUARIO: {self.user}"
              + f"\n\tVEHICULO: {self.car}"
              + f"\n\tRUTA: {self.route}"
              + f"\n\tMETODO DE PAGO: {self.payment}\n")