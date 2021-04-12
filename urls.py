import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants import URL
from constants import URL_CATEGORY


""" Fonction qui recherche les catégories avec les modules resquests,
    beautifulsoup et urllib.parse. Renvoie une liste d'urls des catégories."""


def search_category():

    list_urls_catategories = list()
    url_category = URL
    # Création objet requests.get permet de récupérer une page web.
    response = requests.get(url_category)

    if response.ok:
        # Création du soup qui va analyser le code HTML du site internet.
        soup = BeautifulSoup(response.text, 'html.parser')
        # Recherche de la class contenant les catégories.
        category = soup.find('ul', {'class', 'nav nav-list'}).find('li')\
            .find('ul').findAll('li')
        # Création d'une boucle pour récupérer toutes les catégories.

        for li in category:
            a = li.find('a')
            link = a['href']
            # Création de la variable contenant le nom + mise en forme.
            name_cat = a.text.replace('\n',  '')
            name_categories = name_cat.strip()
            # Utilisation urljoin pour avoir l'adresse complète.
            url_complete = urljoin(URL, link)
            # Création des dicts avec les infos. Important pour la suite.
            names_and_urls = {
                                'name_category': name_categories,
                                'url_category': url_complete
                              }
            # Intégration des dicts à une liste (un dict une catégorie).
            list_urls_catategories.append(names_and_urls)

    return list_urls_catategories


""" Fonction qui recherche si une catégorie contient plusieurs pages.
    Utilisation des modules resquests, beautifulsoup et urllib.parse
    Renvoie une liste d'urls des catégories avec toutes leurs pages."""


def search_pages_category(dict_urls):

    """dict_urls = dict of urls from search_category() """

    # L'objet Session() permet de conserver des paramètres entre plusieurs
    # requêtes. Ensuite on lui envoi une url et il cherche s'il y a
    # d'autres pages.
    with requests.Session() as session:
        links = list()
        url = dict_urls
        links.append(url)
        while True:
            response = session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Regarde s'il y a d'autres pages.
            next_link = soup.find("a", text="next")
            # Si dernière page ou pas de page, il s'arrête.
            if next_link is None:
                break
            # On complète les urls avec urljoin.
            url = urljoin(url, next_link["href"])
            # On renvoi une list des urls des pages.
            links.append(url)

    return links


""" Fonction qui recherche les urls des livres.
    Utilisation des modules resquests, beautifulsoup.
    Renvoie une liste d'urls de livre. """


def search_books(urls_cat_pages):

    """ urls_cat_pages = list of all pages categories
        from search_pages_category() """

    links_books = list()
    # Création d'une boucle qui cherche les livres dans une page.
    for elem in urls_cat_pages:
        response = requests.get(elem)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_class = soup.findAll("article")
        # Création d'une boucle qui cherche les urls des livres.

        for article in article_class:
            a = article.find("a")
            link = a["href"]
            # Mise en forme des urls et place les urls dans une list.
            links_books.append(URL_CATEGORY + link.replace('../../../', ''))

    return links_books
