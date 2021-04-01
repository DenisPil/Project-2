from def_find_all_pages_for_one_category import\
     find_all_pages_for_one_category


# Fonction qui créé une list de dict avec toutes les pages des catégories.
def make_list_of_dict_for_all_cat_all_pages(listX):

    """ listX = list of dict from def get_urls_for_all_cat() """

    dict_pages = {}
    list_dict_cat_pages = []
    # La list de base qui sera utilisé dans la fonction.
    cat = listX
    # Création d'une boucle pour sélectionner une catégories.
    for elem in cat:
        url_cat = (elem['url_category'])
        name_cat = (elem['name_category'])
        # On envoie l'élément url_cat a la fonction "recherche de pages".
        find_all_pages_for_one_category(url_cat)
        # Création des dict qui récupèrent toutes les urls des pages.
        dict_pages = {
            'name_category': name_cat,
            'url_category': find_all_pages_for_one_category(url_cat)
            }
        # On ajoute tous les dict a une list qui contient toutes les pages
        # de toutes les catégories.
        list_dict_cat_pages.append(dict_pages)

    return list_dict_cat_pages
