from services.currency_converter import CurrencyConverter
from services.currency_source import CurrencySource

if __name__ == '__main__':
    cs = CurrencySource('https://api.nbp.pl/api/exchangerates/tables/A/')
    c = CurrencyConverter(cs)

    amount = 1000
    code1, code2 = 'USD', 'EUR'
    res = c.convert(code1, code2, amount)
    print(f'{amount} {code1} = {res} {code2}')