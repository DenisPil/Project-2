from def_scrap_urls_categories import urls_categories
from def_urls_one_cat_all_pages import urls_one_cat_all_pages
from def_scrap_urls_books import scrap_urls_books
from def_scrap_info_table import scrap_info_table
from def_save_info import save_info


def blabla(elema):
    jeanjean = elema

    print(jeanjean)
    return(jeanjean)


def scrap_urls():

    urlX = urls_one_cat_all_pages(blabla())

    return urlX


def scrap_books_urls():

    urls_books = scrap_urls_books(scrap_urls())

    return urls_books


def info_books():

    books = scrap_info_table(scrap_books_urls())

    return books


def save():

    books_in_csv = save_info('', info_books())


def test():

    dico = urls_categories()
    for keys, elem in dico.items():
        jeanjean = blabla(elem)
        print(keys)
        urlX = urls_one_cat_all_pages(blabla(elema))
        urls_books = scrap_urls_books(scrap_urls())
        books = scrap_info_table(scrap_books_urls())
        books_in_csv = save_info('All-books-cat-' + keys + '.csv', info_books())


if __name__ == '__main__':

    test()
