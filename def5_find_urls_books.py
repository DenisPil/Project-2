from bs4 import BeautifulSoup
import requests
from constants import URL_Cat


def find_urls_books(urlX="url pages one cat"):
    url = urlX
    links_books = []

    for i in url:
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_class = soup.findAll("article")

        for article in article_class:
            a = article.find("a")
            link = a["href"]
            links_books.append(URL_Cat + link.replace('../../../', ''))

    # print(len(links_books))
    return(links_books)


if __name__ == '__main__':

    find_urls_books(urlX="url pages one cat")
