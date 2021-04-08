from pathlib import Path
import os
import csv
from constants import FIELDNAMES
from constants import DIRECTORY
from urllib.request import build_opener


# Fonction qui créee un répertoire.
def create_directory():

    path = Path('book_to_scrap')
    try:
        path.mkdir()
    except FileExistsError:
        pass
    directory = Path.cwd() / path

    return directory


# Fonction qui créee et ajoute les informations.
def create_csv(name, info):

    with open(
        name + '.csv', 'w',  encoding='utf-8-sig', newline='')\
            as csvfile:

        fieldnames = FIELDNAMES
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        # writeheader() les en-têtes (fieldnames)
        writer.writeheader()
        # Création d'une boucle qui va sauvegarder les informations.
        for elem in info:
            # writerow() prend chaque élement et les classes dans
            # la bonne ligne grâce au nom des en-têtes (fieldnames).
            # Chaque élement crée une nouvelle ligne.
            writer.writerow(elem)


# Fonction qui sauvegarde une image.
def save_images(url_image):

    opener = build_opener()
    # Création d'une boucle qui cherche certaines infos dans un dict.
    for elem in url_image:

        url_book = elem['product_page_url']
        url_image = elem['image_url']
        category = elem['category']
        name = url_book.replace('https://books.toscrape.com/catalogue/', '')\
            .replace('/index.html', '')
        # Création du répertoire où sera copié les images.
        try:
            os.mkdir(DIRECTORY / category)
        except FileExistsError:
            pass
        # Ouverture du répertoire où sera copié les images.
        os.chdir(DIRECTORY / category)
        # Création du nom du fichier avec le nom du livre.
        filename = "{}.png".format(name)
        # On ouvre l'url de l'image et on la copie dans un fichier,
        # si l'image éxiste, on intercepte l'erreur et on passe à autre chose.
        try:
            with opener.open(url_image) as src, open(filename, 'xb') as dst:
                (dst.write(src.read()))
        except FileExistsError:
            pass
    # A la fin du processus on referme le répertoire.
    os.chdir(DIRECTORY)
