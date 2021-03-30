import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants import URL


def get_urls_for_all_cat():

    list_of_dico_namecat_urlcat = []
    url_category = 'https://books.toscrape.com/index.html'
    response = requests.get(url_category)
    if response.ok:
        list_of_dico_namecat_urlcat = []
        soup = BeautifulSoup(response.text, 'html.parser')
        category = soup.find('ul', {'class', 'nav nav-list'}).find('li')\
            .find('ul').findAll('li')
        for li in category:
            a = li.find('a')
            link = a['href']
            name_categories = a.text.replace('\n',  '').replace(' ', '')
            url_complete = urljoin(URL, link)
            names_and_links = {'name_category': name_categories, 'url_category': url_complete}
            list_of_dico_namecat_urlcat.append(names_and_links)

    # print(list_of_dico_namecat_urlcat)

    return list_of_dico_namecat_urlcat


if __name__ == '__main__':
    get_urls_for_all_cat()
