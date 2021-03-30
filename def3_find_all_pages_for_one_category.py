from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


def find_all_pages_for_one_category(urlX="https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"):

    with requests.Session() as session:
        links = []
        url = urlX
        links.append(url)
        while True:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # regarde si il ya  d'autre pages
            next_link = soup.find("a", text="next")
            if next_link is None:
                break
            url = urljoin(url, next_link["href"])
            links.append(url)

    # print(links, len(links))

    return(links)


if __name__ == '__main__':

    urls_one_cat_all_pages(urlX="https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
