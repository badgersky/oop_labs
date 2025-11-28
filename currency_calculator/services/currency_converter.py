import services.currency_source as currency_source

class CurrencyConverter:

    def __init__(self, source: currency_source):
        self.source = source
    
    def convert(self, from_c: str, to_c: str, amout: float):
        currencies = self.source.get_currencies()

        from_cur = None
        to_cur = None

        for c in currencies:
            if c.code.strip() == from_c.upper():
                from_cur = c
            if c.code.strip() == to_c.upper():
                to_cur = c

        if from_cur is None or to_cur is None:
            print('Currency not found')
            return -1
        
        pln = amout * from_cur.rate
        return pln / to_cur.rate