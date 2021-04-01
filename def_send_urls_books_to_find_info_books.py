from def_get_info_for_one_book import get_info_book
from def_get_image import create_repertory
from def_create_csv import create_csv


# Fonction qui envoie a une autre fonction des urls de livres pour
# trouver des informations.
def send_urls_books_to_find_info_books(listX):

    """ listX = list of dict from send_urls_pages_to_find_urls_books()"""

    dict_all_info = {}
    list_all_info = []
    urls_books = listX
    # Création boucle qui cherche certain élément.
    for elem in urls_books:
        url_book = (elem['url_book'])
        name_cat = (elem['name_category'])
        # utilisation de l'élément 'name_category' pour créé un
        # répertoire et le fichier .csv
        create_repertory(name_cat)
        create_csv(name_cat + '.csv')
        # Création d'une autre boucle qui va envoyer les urls de tous les
        # livres une par une pour récuperer les informations et
        # les classer dans des dicts.
        for url in url_book:
            get_info_book(url)

            dict_all_info = {
                                'category': name_cat,
                                'books_info': get_info_book(url)
                            }
            # On envoie tous les dict a une list.
            list_all_info.append(dict_all_info)

    return list_all_info
