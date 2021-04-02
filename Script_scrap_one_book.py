from def_send_urls_pages_to_find_urls_books import\
     send_urls_pages_to_find_urls_books
from def_send_urls_books_to_find_info_books import\
     send_urls_books_to_find_info_books
from def_save_info_in_csv import save_info_in_csv
from constants import BOOK


def urls_books_find_info_books():
    info = []
    dict_all_info = {'name_category': 'Poetry', 'url_book': BOOK}
    info.append(dict_all_info)
    info_books = send_urls_books_to_find_info_books(info)

    return info_books


def save_one_book():
    save = save_info_in_csv(urls_books_find_info_books())

    return 0


if __name__ == '__main__':
    save_one_book()
