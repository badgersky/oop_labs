class Currency:

    def __init__(self, code: str, name: str, rate: float):
        self.code = code
        self.name = name
        self.rate = rate

    def __str__(self):
        return f'Currency: {self.name}, code: {self.code}, rate: {self.rate}'