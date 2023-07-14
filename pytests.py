from bs4 import BeautifulSoup
import requests
from parser import get_html_soup, privat_usd


def test_get_html_soup():
    # Arrange
    url = "https://example.com"

    # Act
    soup = get_html_soup(url)

    # Assert
    assert isinstance(soup, BeautifulSoup)

def test_privat_usd():
    # Arrange
    html = """
    <html>
    <body>
    <td class="js-ex-rates" data-title="1.23">USD</td>
    </body>
    </html>
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Act
    result = privat_usd(soup)

    # Assert
    assert result == "1.23"
