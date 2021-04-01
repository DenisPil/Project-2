from def_get_urls_categories import get_urls_for_all_cat
from def_make_list_of_dict_for_all_cat_all_pages import\
     make_list_of_dict_for_all_cat_all_pages
from def_send_urls_pages_to_find_urls_books import\
     send_urls_pages_to_find_urls_books
from def_send_urls_books_to_find_info_books import\
     send_urls_books_to_find_info_books
from def_save_info_in_csv import save_info_in_csv


def get_urls_categories():
    urls_pages = get_urls_for_all_cat()

    return urls_pages


def make_list_of_dict_all_pages():
    make_list = make_list_of_dict_for_all_cat_all_pages(get_urls_categories())

    return make_list


def send_pages_find_urls_books():
    urls_books = send_urls_pages_to_find_urls_books(
        make_list_of_dict_all_pages())

    return urls_books


def urls_books_find_info_books():
    info_books = send_urls_books_to_find_info_books(
        send_pages_find_urls_books())

    return info_books


def save_in_csv():
    save = save_info_in_csv(urls_books_find_info_books())


if __name__ == '__main__':
    save_in_csv()
