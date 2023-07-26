import requests
from bs4 import BeautifulSoup
from langdetect import detect
import pycountry
from itc_top_material import URL

# URL = 'https://github.com/Vict0rt'
# URL = input('Please enter URL for detect content language: ')

def get_website_language(url=URL):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    text=soup.get_text()

    return text

def site_language(text_from_site=get_website_language()):
    language_code = detect(text_from_site)
    language_name = pycountry.languages.get(alpha_2=language_code).name

    return print(f'This site contented by {language_name} language.')


def main():
    web_content = get_website_language()
    return site_language(web_content)


if __name__ == "__main__":
    main()
