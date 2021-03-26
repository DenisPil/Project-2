import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants import URL


def urls_categories():

    url_category = 'https://books.toscrape.com/index.html'
    response = requests.get(url_category)
    if response.ok:
        links_categories = {}
        soup = BeautifulSoup(response.text, 'html.parser')
        category = soup.find('ul', {'class', 'nav nav-list'}).find('li')\
            .find('ul').findAll('li')
        for li in category:
            a = li.find('a')
            link = a['href']
            name_categories = a.text.replace('\n',  '').replace(' ', '')
            url_complete = urljoin(URL, link)
            names_and_links = {name_categories: url_complete}
            links_categories.update(names_and_links)
    # print(links_categories)
    return(links_categories)


if __name__ == '__main__':
    urls_categories()
