from def_append_csv import append_csv
from def_get_image import save_images


# Fonction qui va envoyer les éléments a d'autres fonctions.
# Permet aux autres fonctions de traiter les éléments un par un.
def save_info_in_csv(listX):

    """ listX = list of dict from send_urls_books_to_find_info_books()"""

    category = listX
    # Création d'une boucle qui va envoyer les éléments.
    for elem in category:

        append_csv(elem)
        save_images(elem)

    return 0
