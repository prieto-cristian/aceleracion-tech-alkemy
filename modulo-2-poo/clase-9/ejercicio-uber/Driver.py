from Account import Account


class Driver(Account):
    def __init__(self,id: int, name: str, email: str, license_driver: str):
        super().__init__(id, name, email)
        self.license_driver = license_driver

    def __str__(self):
        return (super().__str__()
                + f", Licencia conductor: {self.license_driver}")