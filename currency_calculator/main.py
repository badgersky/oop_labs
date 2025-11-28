from services.CurrencySource import CurrencySource

if __name__ == "__main__":
    cs = CurrencySource("https://api.nbp.pl/api/exchangerates/tables/A/")

    rates = cs.get_currencies()
    for rate in rates:
        print(rate)