import requests
from models.currency import Currency

class CurrencySource:

    def __init__(self, url: str):
        self.url = url

    def get_currencies(self):
        response = requests.get(self.url)
        data = response.json()

        rates_list = data[0]['rates']

        currencies = []
        for rate in rates_list:
            currency = Currency(
                code=rate['code'],
                name=rate['currency'],
                rate=rate['mid']
            )
            currencies.append(currency)

        return currencies