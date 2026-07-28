class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        # Para indicar que el saldo es privado. Y si tiene un solo guion bajo?
        self.__saldo = saldo

    def obtener_saldo(self):
        return f"El saldo de {self.titular} es : ${self.__saldo}"

    def retirar_dinero(self, monto):
        if 0 <= monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso de ${monto}.")
            print(f"Saldo restante: {self.__saldo}")
        else:
            print("Fondos insuficientes")

cuenta1 = CuentaBancaria("Rogelio", 300000)
print(cuenta1.obtener_saldo())

cuenta1.retirar_dinero(100000)
print(vars(cuenta1))