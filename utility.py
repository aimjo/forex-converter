import requests


def is_valid_currency(currency_code):
    '''Check to see if currency code is valid
    USD, EUR, GBP, JPY, CAD, MXN'''
    api_url = f"https://api.exchangerate.host/{currency_code}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return True
    return False

def convert_currency(amount, from_currency, to_currency,):
    '''Converts currency'''
    api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(api_url)
    data = response.json()
    if response.status_code == 200:
        converted_amount = data['result']
        return round(converted_amount, 2)
    return None

def get_currency_symbol(currency_code):
    '''Gets currency symbol'''
    symbols_url = 'https://api.exchangerate.host/symbols'
    response = requests.get(symbols_url)
    if response.status_code == 200:
        symbols_data = response.json()
        currency_info = symbols_data['symbols'].get(currency_code)
        if currency_info:
            return currency_info.get('symbol', currency_code)
    return None