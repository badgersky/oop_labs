class Currency:

    def __init__(self, code, name, rate):
        self.__code = code
        self.__name = name
        self.__rate = rate

    def __str__(self):
        return f"Currency: {self.name}, code: {self.code}, rate: {self.rate}"