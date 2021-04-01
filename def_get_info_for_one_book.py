from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from constants import URL


# Fonction qui récolte les informations d'un a partir d'une url
def get_info_book(urlX):

    """ urlX = elem from list, from send_urls_books_to_find_info_books()."""

    url = urlX
    prod_info = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # recherche d'une partie des information présente sur la page
    title = soup.find('h1').text
    product_description = soup.findAll('p')[3].text.replace('\n', '')
    review_rating = soup.find('p', class_='star-rating')['class'][1]
    category = soup.find('ul', {'class': 'breadcrumb'})\
        .findAll('li')[2].text.replace('\n', '')

    image_url_no_join = soup.find('img', src_='')['src']
    image_url = urljoin(URL, image_url_no_join)
    # Création d'un dict qui contiendra toutes les informations
    info_dico = {
        'product_page_url': url,
        'title': title,
        'product_description': product_description,
        'category': category,
        'review_rating': review_rating,
        'image_url': image_url
            }
    # Création d'une variable qui cherche les infos dans 'table table-striped'.
    product_information = soup.find('table', {'class': 'table table-striped'})\
        .findAll('tr')
    # Création d'un dict qui récupere les infos de la fonction process_tr.
    dict_prod_information = process_tr(product_information)
    # On rassemble les deux dict pour avoir un seul dict avec toutes les infos.
    info_dico.update(dict_prod_information)
    # Le dict est ensuite ajouter a une list.
    prod_info.append(info_dico)

    return prod_info


# Fonction qui cherche les informations grave a la variable créé plus haut.
def process_tr(product_information):

    """ product_information = variable ligne 35. """

    info_dico = dict()
    for prod in product_information:
        th = prod.find('th').text.replace(' ', ('_'))
        td = prod.find('td').text.replace('In stock', '')
        # Si une information est manquante on l'indique.
        if td == '':
            td = ('no info')
        one_info = {th: td}
        info_dico.update(one_info)

    return info_dico
