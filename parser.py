from bs4 import BeautifulSoup
import requests


URL = "https://minfin.com.ua/ua/currency/banks/"


def get_html_soup(url=URL):
    if URL == '':
        print('The URL is empty.')
        exit(1)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup


def privat_usd(html_soup_content=get_html_soup(url=URL)):
    try:
        all_private = html_soup_content.find('td', class_=['js-ex-rates'])
        usd_privat = all_private['data-title']
    except TypeError as error:
        print(error)
        print("Cannot find element on the page.")
        exit(1)
    return usd_privat


def main():
    soup = get_html_soup()
    print(privat_usd(soup))


if __name__ == "__main__":
    main()
