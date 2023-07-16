from bs4 import BeautifulSoup
import requests


URL = "https://itc.ua/ua/"

def get_html_soup(url=URL):
    if URL == '':
        print('The URL is empty.')
        exit(1)
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

def top_site_material():
    soup = get_html_soup()
    h2_element = soup.find('div', class_=["col-xs-12 col-lg-8"]).find('h2')
    desired_text = h2_element.a.get_text(strip=True)
    link = h2_element.a['href']
    return [desired_text, link]

def main():
    print(*top_site_material(), sep='\n')


if __name__ == "__main__":
    main()

