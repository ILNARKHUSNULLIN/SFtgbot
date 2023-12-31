import json
import requests
from config import curs


class DataValidationException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            base_key = curs[base.lower()]
        except KeyError:
            e = f'Валюта {base} не найдена.'
            raise DataValidationException(e)

        try:
            quote_key = curs[quote.lower()]
        except KeyError:
            e = f'Валюта {quote} не найдена.'
            raise DataValidationException(e)

        if base_key == quote_key:
            e = 'Невозможно конвертировать одинаковые валюты.'
            raise DataValidationException(e)

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            e = f'Не удалось обработать количество «{amount}».'
            raise DataValidationException(e)

        r = requests.get('https://open.er-api.com/v6/latest/USD')
        data = json.loads(r.content)
        if base_key == 'USD':
            result = amount * data['rates'][quote_key]
        else:
            result = amount * data['rates'][quote_key] * (1 / data['rates'][base_key])
        return f'{amount} {base} → {result} {quote}'