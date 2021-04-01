from def_make_list_of_dict_for_all_cat_all_pages import\
     make_list_of_dict_for_all_cat_all_pages
from def_send_urls_pages_to_find_urls_books import\
     send_urls_pages_to_find_urls_books
from def_send_urls_books_to_find_info_books import\
     send_urls_books_to_find_info_books
from def_save_info_in_csv import save_info_in_csv
from constants import CATEGORY


def make_list_of_dict_all_pages():
    list_of_dico_namecat_urlcat = []
    names_and_links = {
                        'name_category': 'Sequential Art',
                        'url_category': CATEGORY
                        }
    list_of_dico_namecat_urlcat.append(names_and_links)
    make_list = make_list_of_dict_for_all_cat_all_pages(
        list_of_dico_namecat_urlcat)

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

    return 0


if __name__ == '__main__':
    save_in_csv()
