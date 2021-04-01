import csv
from constants import FIELDNAMES


# Fonction qui ajoute les informations au fichier déjâ créé.
def append_csv(info):

    """ info = dict from def save_info_in_csv(). """

    with open(
        info['category'] + '.csv', 'a',  encoding='utf-8-sig', newline='')\
            as csvfile:

        fieldnames = FIELDNAMES
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        # Création d'une boucle qui va sauvegarder les informations.
        for elem in info['books_info']:
            # writerow() prend chaque élement et les classes dans
            # la bonne lignes grace au nom des entêtes (fieldnames).
            # Chaque élement crée une nouvelle ligne.
            writer.writerow(
                    {
                        'product_page_url': elem['product_page_url'],
                        'universal_product_code': elem['UPC'],
                        'title': elem['title'],
                        'price_including_tax': elem['Price_(incl._tax)'],
                        'price_excluding_tax': elem['Price_(excl._tax)'],
                        'number_available': elem['Availability'],
                        'product_description': elem['product_description'],
                        'category': elem['category'],
                        'review_rating': elem['review_rating'],
                        'image_url': elem['image_url']
                    }
                )
    return 0
