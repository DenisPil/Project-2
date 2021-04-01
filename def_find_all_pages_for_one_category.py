from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin


# Fonction qui cherche si une catégories a plusieurs pages.
def find_all_pages_for_one_category(urlX):

    """ urlX = elem from dict,
        from make_list_of_dict_for_all_cat_all_pages()"""

    # L'objet Session() permet de conserver des paramètres entre plusieurs
    # requêtes. Ensuite on lui envoie une url et il cherche si il y a
    # d'autre pages.
    with requests.Session() as session:
        links = []
        url = urlX
        links.append(url)
        while True:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Regarde si il y a  d'autre pages.
            next_link = soup.find("a", text="next")
            # Si plus ou pas de page il s'arrete.
            if next_link is None:
                break
            # On complète les urls avec urljoin.
            url = urljoin(url, next_link["href"])
            # On renvoie une list des urls des pages.
            links.append(url)

    return links
