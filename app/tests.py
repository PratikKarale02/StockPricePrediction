from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
import unittest
from unittest.mock import patch
import yfinance as yf
#python manage.py test --verbosity 2


class UserLoginTest(TestCase):

    def setUp(self):
        #self.login_url = reverse('login')
        self.username = 'Pratik692002@gmail.com'
        self.password = 'Pratik2002'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_login(self):
        # Send a POST request with the user's credentials
        login_data = {
            'username': self.username,
            'password': self.password
        }
        

    def test_user_login_with_invalid_credentials(self):
        # Send a POST request with invalid credentials
        login_data = {
            'username': self.username,
            'password': 'invalidpassword'
        }

    def test_user_registration(self):
        # Create a test user
        user_data = {
            'username': 'Pratik692002@gmail.com',  # Gmail address
            'password1': 'Pratik2002',
            'password2': 'testpassword'
        }
        
    def test_user_registration_with_missing_data(self):
        # Create a test user with missing data
        user_data = {
            'username': 'testuser',
            'password2': 'testpassword'
        }
        

class AdminLoginTest(TestCase):
    def setUp(self):
        #self.login_url = reverse('login')
        self.username = 'admin@stockprice.com'
        self.password = '123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_user_login(self):
        # Send a POST request with the user's credentials
        login_data = {
            'username': self.username,
            'password': self.password
        }

    def test_user_login_with_invalid_credentials(self):
        # Send a POST request with invalid credentials
        login_data = {
            'username': self.username,
            'password': 'invalidpassword'
        }
def get_company_ticker(symbol):
    ticker = yf.Ticker(symbol)
    return {
        'symbol': ticker.info['symbol'],
        'name': ticker.info['longName']
    }


class CompanyTickerTest(unittest.TestCase):

    @patch('yfinance.Ticker')
    def test_get_company_ticker(self, mock_yfinance_ticker):
        # Mock the response from yfinance
        mock_yfinance_ticker.return_value.info = {
            'symbol': 'WIPRO',
            'longName': 'Wipro Limited '
        }

        # Call the function to retrieve company ticker information
        ticker = get_company_ticker('WIPRO')
        # Call the function to retrieve company ticker information
        ticker = get_company_ticker('WIPRO')

        # Check if the ticker is retrieved correctly
        self.assertEqual(ticker['symbol'], 'WIPRO')
        self.assertEqual(ticker['name'], 'Wipro Limited ')


if __name__ == '__main__':
    unittest.main()




def get_company_ticker(symbol):
    ticker = yf.Ticker(symbol)
    if 'symbol' in ticker.info:
        return {
            'symbol': ticker.info['symbol'],
            'name': ticker.info['longName']
        }
    else:
        return None


class CompanyTickerTest(unittest.TestCase):

    @patch('yfinance.Ticker')
    def test_get_company_ticker(self, mock_yfinance_ticker):
        # Mock the response from yfinance for a valid ticker
        mock_yfinance_ticker.return_value.info = {
            'symbol': 'AAPL',
            'longName': 'Apple Inc.'
        }

        # Call the function to retrieve company ticker information for a valid ticker
        ticker = get_company_ticker('AAPL')

        # Check if the ticker is retrieved correctly
        self.assertEqual(ticker['symbol'], 'AAPL')
        self.assertEqual(ticker['name'], 'Apple Inc.')

    @patch('yfinance.Ticker')
    def test_get_company_ticker_with_invalid_ticker(self, mock_yfinance_ticker):
        # Mock the response from yfinance for an invalid ticker
        mock_yfinance_ticker.return_value.info = {}

        # Call the function to retrieve company ticker information for an invalid ticker
        ticker = get_company_ticker('INVALID')

        # Check if the ticker is None when an invalid ticker is provided
        self.assertIsNone(ticker)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
import yfinance as yf


def download_dataset(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period='1d')
    # Perform additional processing or save the data
    return data


class DatasetDownloadTest(unittest.TestCase):

    @patch('yfinance.Ticker')
    def test_download_dataset(self, mock_yfinance_ticker):
        # Mock the response from yfinance
        mock_yfinance_ticker.return_value.history.return_value = 'Mocked dataset'

        # Call the function to download the dataset
        data = download_dataset('AAPL')

        # Check if the dataset is retrieved correctly
        self.assertEqual(data, 'Mocked dataset')


if __name__ == '__main__':
    unittest.main()




        