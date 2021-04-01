import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from constants import URL


# Première fonction lance la recherche de catégories
def get_urls_for_all_cat():

    list_of_dico_namecat_urlcat = []
    url_category = 'https://books.toscrape.com/index.html'
    # création objet requests.get permet de récupérer une page web
    response = requests.get(url_category)

    if response.ok:
        # création du soup qui va analyser le code HTML du site internet
        soup = BeautifulSoup(response.text, 'html.parser')
        # recherche de la class contenant les catégories
        category = soup.find('ul', {'class', 'nav nav-list'}).find('li')\
            .find('ul').findAll('li')
        # création d'une boucle pour récupérer toutes les catégories
        for li in category:
            a = li.find('a')
            link = a['href']
            # création de la variable contenant le nom + (mise en forme)
            name_cat = a.text.replace('\n',  '')
            name_categories = name_cat.strip()
            # utilisation urljoin pour avoir l'adresse complète
            url_complete = urljoin(URL, link)
            # création des dict avec les infos !! important pour la suite
            names_and_links = {
                                'name_category': name_categories,
                                'url_category': url_complete
                                }
            # intégration des dicts a une liste (un dict une catégories)
            list_of_dico_namecat_urlcat.append(names_and_links)

    return list_of_dico_namecat_urlcat
