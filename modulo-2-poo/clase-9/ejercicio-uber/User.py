from Account import Account
class User(Account):
    def __init__(self, id: int, name: str, email: str):
        super().__init__(id, name, email)

    def __str__(self):
        return super().__str__()