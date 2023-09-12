import unittest
from flask import Flask
import requests
from flask_testing import TestCase
from utility import is_valid_currency, convert_currency, get_currency_symbol
from app import create_app


class TestCurrencyConverterApp(TestCase):
    def setUp(self):
        # Create a test client for the Flask application
        app = create_app()
        self.client = app.test_client()

    def test_valid_currency(self):
        '''Test to see if we can make a valid request'''
        currency_code = 'USD'
        result = is_valid_currency(currency_code)
        self.assertTrue(result)

    def test_invalid_currency(self):
        '''Test to see if we can make an invalid request'''
        currency_code = 'INVALID'
        result = is_valid_currency(currency_code)
        self.assertFalse(result)

    def test_convert_currency_success(self):
        '''Testing valid conversion'''
        amount = 100
        from_currency = 'USD'
        to_currency = 'EUR'

        # API request
        response = requests.get(f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}")

        self.assertEqual(response.status_code, 200)

        data = response.json()
        converted_amount = data['result']

        # Check if the converted amount is a positive number
        self.assertTrue(converted_amount > 0) 

    def test_convert_currency_failure(self):
        '''Test convert currency invalid response'''
        amount = 100
        from_currency = 'USD'
        to_currency = 'INVALID'

        # Make an actual API request
        response = requests.get(f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}")

        self.assertNotEqual(response.status_code, 200)

        # Ensure that the response data is empty (indicating a failure)
        self.assertEqual(response.text, '')

    def test_convert_usd_to_usd(self):
        '''Tests conversion using 1 USD to 1 USD'''
        amount = 1  # Any amount
        from_currency = 'USD'
        to_currency = 'USD'

        # Make an actual API request
        api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(api_url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        converted_amount = data['result']

        self.assertEqual(converted_amount, 1.00)


    