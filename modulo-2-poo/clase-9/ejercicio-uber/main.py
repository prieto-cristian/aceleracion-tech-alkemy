from Trip import Trip
from User import User
from Driver import Driver
from UberBlack import UberBlack
from UberX import UberX
from UberVan import UberVan
from UberPool import UberPool
from Route import Route
from Efectivo import Efectivo
from Tarjeta import Tarjeta
from PayPal import PayPal
##############################################################################

# Definicion de usuarios
user1 = User(1, "Cristian", "cristian@gmail.com")
user2 = User(2, "Andres", "andres@gmail.com")
user3 = User(3, "Lucas", "lucas@gmail.com")

# Definicion de conductores
driver1 = Driver(1, "Marcelo", "marcelo@gmail.com", "Tipo A")
driver2 = Driver(2, "Patricio", "patricio@gmail.com", "Tipo B")
driver3 = Driver(3, "Aldana", "aldana@gmail.com", "Tipo C")
driver4 = Driver(4, "Laura", "laura@gmail.com", "Tipo D")

# Definicion de carros
car1 = UberBlack(1, "XYZ-123", driver1, "Cuero")
car2 = UberPool(2, "ABC-789", driver2, "Toyota", "Corolla")
car3 = UberX(3, "DDD-111", driver3, "Hyundai", "Creta")
car4 = UberVan(4, "FFF-999", driver4, 12)

# Definicion de rutas
route1 = Route("Cipolletti", "Villa Regina")
route2 = Route("Bariloche", "Viedma")
route3 = Route("Luis Beltran", "Pomona")
route4 = Route("General Roca", "Las grutas")

# Definicion de metodos de pagos
payment1 = Efectivo(1, 12150)
payment2 = Tarjeta(1, 130000, "XXXX-XXXX-XXXX-1232", 111)
payment3 = PayPal(1, 76000, "aaaaa@gmail.com")
payment4 = PayPal(1, 55000, "emisorpaypal@gmail.com")

# Definicion de viajes
viaje1 = Trip(1, user1, car1, route1, payment1)
viaje2 = Trip(2, user2, car2, route2, payment2)
viaje3 = Trip(3, user3, car3, route3, payment3)
viaje4 = Trip(4, user1, car4, route4, payment4)

# Mostrar resultados
viaje1.summary()
viaje2.summary()
viaje3.summary()
viaje4.summary()


##############################################################################
