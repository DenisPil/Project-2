from def_urls_one_cat_all_pages import urls_one_cat_all_pages
from def_scrap_urls_books import scrap_urls_books
from def_scrap_info_table import scrap_info_table
from def_save_info import save_info


def scrap_urls():

    urlX = urls_one_cat_all_pages('https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html')

    return urlX


def scrap_books_urls():

    urls_books = scrap_urls_books(scrap_urls())

    return urls_books


def info_books():

    books = scrap_info_table(scrap_books_urls())

    return books


def save():

    books_in_csv = save_info('All-books-cat-Nonfiction.csv', info_books())


if __name__ == '__main__':

    save()
