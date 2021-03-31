from def2_make_list_of_dict_for_all_cat_all_pages import make_list_of_dict_for_all_cat_all_pages
from def5_find_urls_books import find_urls_books


def send_urls_pages_to_find_urls_books(def2):

    dict_urls_pages_books_and_name_cat = {}
    listdict_cat_name_and_urls_pages_books = []
    urls_pages = def2

    for elem in urls_pages:
        url_cat = (elem['url_category'])
        name_cat = (elem['name_category'])
        find_urls_books(url_cat)

        dict_urls_pages_books_and_name_cat = {'name_category': name_cat, 'url_category': url_cat, 'url_book': find_urls_books(url_cat)}
        listdict_cat_name_and_urls_pages_books.append(dict_urls_pages_books_and_name_cat)

    # print(listdict_cat_name_and_urls_pages_books)

    return(listdict_cat_name_and_urls_pages_books)


if __name__ == '__main__':

    send_urls_pages_to_find_urls_books()
