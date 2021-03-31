from def4_send_urls_pages_to_find_urls_books import send_urls_pages_to_find_urls_books
from def6_send_urls_books_to_find_info_books import send_urls_books_to_find_info_books
from def8_save_info_in_csv import save_info_in_csv
from constants import BOOK_TEST


def urls_books_find_info_books():
    info = []
    dict_all_info = {'name_category': 'A Light in the Attic', 'url_book': BOOK_TEST}
    info.append(dict_all_info)
    info_books = send_urls_books_to_find_info_books(info)
    print(info)

    return info_books


def save_in_csv():
    save = save_info_in_csv(urls_books_find_info_books())

    return 0


if __name__ == '__main__':
    save_in_csv()
