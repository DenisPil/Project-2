from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
from constants import URL


""" Fonction qui recherche une partie des informations d'un livre.
    Utilisation des modules resquests, beautifulsoup.
    Renvoie une liste contenant toutes les informations d'un livre."""


def search_info(urls_book):

    """urls_book = list of urls books from search_books()"""

    prod_info = list()

    for url in urls_book:

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Recherche d'une partie des informations présentes sur la page.
        title = soup.find('h1').text
        product_description = soup.findAll('p')[3].text.replace('\n', '')
        review_rating = soup.find('p', class_='star-rating')['class'][1]
        category = soup.find('ul', {'class': 'breadcrumb'})\
            .findAll('li')[2].text.replace('\n', '')
        image_url_no_join = soup.find('img', src_='')['src']
        image_url = urljoin(URL, image_url_no_join)
        # Création d'un dict qui contiendra toutes les informations.
        info_dico = {
            'product_page_url': url,
            'title': title,
            'product_description': product_description,
            'category': category,
            'review_rating': review_rating,
            'image_url': image_url
                }
        # Création d'une variable qui cherche dans 'table table-striped'.
        product_information = soup.find('table',
                                        {'class':
                                            'table table-striped'})\
            .findAll('tr')
        # Création d'un dict qui récupère les infos de la fonction process_tr.
        dict_prod_information = process_tr(product_information)
        # On rassemble les deux dict avec toutes les infos.
        info_dico.update(dict_prod_information)
        # Le dict est ensuite ajouté à une list.
        prod_info.append(info_dico)

    return prod_info


""" Fonction qui recherche une autre partie des informations d'un livre.
    les informations sont modifié (changement de noms
    suppression de ce qui est inutile).
    Renvoie un dict contenant les informations de 'table-striped' """


def process_tr(product_information):

    """ product_information = variable from search_info(), this variable looks
        for book information in the 'table table-striped' section """

    info_dico = dict()

    for prod in product_information:
        th = prod.find('th').text.replace(' ', ('_'))
        td = prod.find('td').text.replace('In stock', '')
        # Si une information est manquante, on l'indique.
        if td == '':
            td = ('no info')
        one_info = {th: td}
        info_dico.update(one_info)

    # Changement : nom de clé et suppression des infos inutiles.
    info_dico['universal_product_code'] = info_dico.pop('UPC')
    info_dico['price_including_tax'] = info_dico.pop('Price_(incl._tax)')
    info_dico['price_excluding_tax'] = info_dico.pop('Price_(excl._tax)')
    info_dico['number_available'] = info_dico.pop('Availability')
    info_dico.pop('Product_Type')
    info_dico.pop('Number_of_reviews')
    info_dico.pop('Tax')

    return info_dico
