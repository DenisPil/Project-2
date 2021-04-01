import os
from urllib.request import build_opener


# Fonction de création de répertoire.
def create_repertory(name_rep):

    """ name_rep = list of dict from send_urls_books_to_find_info_books()"""

    name = name_rep
    # Création du répertoire mais si le répertoire existe déjà on réléve
    # l'erreur et passe a autre chose.
    try:
        os.mkdir(name)
    except FileExistsError:
        pass


# Fonction qui sauvegarde une image.
def save_images(urlX):

    """ urlX = dict from def save_info_in_csv(). """

    url = urlX
    # build_opener() est un moyen simple de définir des en-têtes une seule
    # fois pour toutes les requêtes à envoyer.
    opener = build_opener()
    # Création d'une boucle qui cherche certaines infos dans un dict
    for elem in url['books_info']:
        url_book = elem['product_page_url']
        url_image = elem['image_url']
        category = elem['category']
        name = url_book.replace('https://books.toscrape.com/catalogue/', '')\
            .replace('/index.html', '')
        # Ouverture du répertoire ou sera copier les images.
        os.chdir('C:/OpenClassrooms/Project-2/' + category)
        # Création du nom du fichier avec le nom du livre.
        filename = "{}.png".format(name)
        # On ouvre l'url de l'image et on la copie dans un fichier,
        # si l'image éxiste déjà on l'erreur et passe a autre chose.
        try:
            with opener.open(url_image) as src, open(filename, 'xb') as dst:
                (dst.write(src.read()))
        except FileExistsError:
            pass
    # A la fin du processus on referme le répertoire.
    os.chdir('C:/OpenClassrooms/Project-2/')

    return 0
