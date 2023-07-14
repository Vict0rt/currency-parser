'''doc is coming soon'''
from bs4 import BeautifulSoup
import requests


def privat_usd():
    URL = "https://minfin.com.ua/ua/currency/banks/"

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    all_private = soup.find('td', class_=['js-ex-rates'])
    usd_privat = all_private['data-title']
    return usd_privat

