from def_find_urls_books import find_urls_books


# Fonction qui envoie a une autre fonction les urls des pages
# pour trouver les urls des livres.
def send_urls_pages_to_find_urls_books(listX):

    """ listX = list of dict from make_list_of_dict_for_all_cat_all_pages()"""

    dict_urls_pages_books_and_name_cat = {}
    listdict_cat_name_and_urls_pages_books = []
    urls_pages = listX

    for elem in urls_pages:
        url_cat = (elem['url_category'])
        name_cat = (elem['name_category'])
# On envoie les urls des catégories à la fonction qui trouve l'url des livres.
        find_urls_books(url_cat)
# Les urls des livres trouvés on les intègrent a un dict.
        dict_urls_pages_books_and_name_cat = {
            'name_category': name_cat,
            'url_category': url_cat,
            'url_book': find_urls_books(url_cat)
        }
# On ajoute les dict a une list.
        listdict_cat_name_and_urls_pages_books\
            .append(dict_urls_pages_books_and_name_cat)

    return listdict_cat_name_and_urls_pages_books
