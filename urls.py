import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants import URL
from constants import URL_CAT


# Première fonction lance la recherche de catégorie
def urls_cat():

    list_of_dico_namecat_urlcat = []
    url_category = 'https://books.toscrape.com/index.html'
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
            names_and_links = {
                                'name_category': name_categories,
                                'url_category': url_complete
                              }
            # Intégration des dicts à une liste (un dict une catégorie).
            list_of_dico_namecat_urlcat.append(names_and_links)

    return list_of_dico_namecat_urlcat


# Fonction qui cherche si une catégorie a plusieurs pages.
def pages_category(dict_urls):

    # L'objet Session() permet de conserver des paramètres entre plusieurs
    # requêtes. Ensuite on lui envoi une url et il cherche s'il y a
    # d'autres pages.
    with requests.Session() as session:
        links = []
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


# Fonction qui cherche les urls des livres.
def urls_books(urls_cat_pages):

    url = urls_cat_pages
    links_books = []
    # Création d'une boucle qui cherche les livres dans une page.
    for elem in url:

        response = requests.get(elem)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_class = soup.findAll("article")
        # Création d'une boucle qui cherche les urls des livres.

        for article in article_class:

            a = article.find("a")
            link = a["href"]
            # Mise en forme des urls et place les urls dans une list.
            links_books.append(URL_CAT + link.replace('../../../', ''))

    return links_books
