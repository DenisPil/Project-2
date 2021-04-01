import csv
from constants import FIELDNAMES


# Fonction qui créé le fichier .csv qui contiendra toutes les informations.
def create_csv(file_name):

    """ file_name = elem from dict,
        from send_urls_books_to_find_info_books()."""

    csvfile = open(file_name, 'w',  encoding='utf-8-sig', newline='')
    # Fieldnames le nom des entête du fichier .csv .
    fieldnames = FIELDNAMES
    # DicWriter crée un objet qui produit les lignes de sortie
    # depuis des dictionnaires.
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
    # writhehearder applique les entête en haut de page.
    writer.writeheader()
    csvfile.close()

    return 0
