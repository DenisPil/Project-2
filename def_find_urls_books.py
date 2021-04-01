from bs4 import BeautifulSoup
import requests
from constants import URL_CAT


# Fonction qui cherche les urls des livres.
def find_urls_books(urlX):

    """ urlX = list from send_urls_pages_to_find_urls_books() """

    url = urlX
    links_books = []
    # création d'une boucle qui cherche les livres dans une page.
    for i in url:
        response = requests.get(i)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_class = soup.findAll("article")
        # Création d'une boucle qui cherche les urls des livres.
        for article in article_class:
            a = article.find("a")
            link = a["href"]
            # Mise en forme des urls et on place les urls dans une list.
            links_books.append(URL_CAT + link.replace('../../../', ''))

    return links_books
