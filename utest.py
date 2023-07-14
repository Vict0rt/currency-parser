import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
import requests
from parser import get_html_soup, privat_usd


class TestPrivatUSD(unittest.TestCase):

    @patch('parser.requests.get')
    @patch('parser.BeautifulSoup')
    def test_privat_usd(self, mock_soup, mock_get):
        mock_response = MagicMock()
        mock_response.content = b'<html><td class="js-ex-rates" data-title="25.00">USD</td></html>'

        mock_get.return_value = mock_response
        mock_soup.return_value = MagicMock(find=MagicMock(return_value=mock_response))

        expected_result = "36.600 / 38.200"
        result = privat_usd()

        self.assertEqual(result, expected_result)
        mock_get.assert_called_once_with("https://minfin.com.ua/ua/currency/banks/")
        mock_soup.assert_called_once_with(mock_response.content, 'html.parser')
        mock_response.content.decode.assert_called_once_with('utf-8')

    @patch('builtins.print')
    def test_get_html_soup_empty_url(self, mock_print):
        expected_output = 'The URL is empty.\n'
        with self.assertRaises(SystemExit) as cm:
            get_html_soup(url='')
            mock_print.assert_called_once_with('The URL is empty.')
        self.assertEqual(cm.exception.code, 1)
        self.assertEqual(mock_print.call_args[0][0], expected_output)


if __name__ == '__main__':
    unittest.main()
