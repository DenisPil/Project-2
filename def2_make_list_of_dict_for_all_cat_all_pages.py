from def1_get_urls_categories import get_urls_for_all_cat
from def3_find_all_pages_for_one_category import find_all_pages_for_one_category

# test =[{'name_category': 'academic','url_category':'https://books.toscrape.com/catalogue/category/books/academic_40/index.html'},{'name_category': 'self-help','url_category': 'https://books.toscrape.com/catalogue/category/books/self-help_41/index.html'}]


def make_list_of_dict_for_all_cat_all_pages():

    dict_pages = {}
    list_dict_cat_pages = []
    cat = get_urls_for_all_cat()

    for elem in cat:
        url_cat = (elem['url_category'])
        name_cat = (elem['name_category'])
        # print(url_cat)
        find_all_pages_for_one_category(url_cat)
        dict_pages = {'name_category': name_cat, 'url_category': find_all_pages_for_one_category(url_cat)} 

        list_dict_cat_pages.append(dict_pages)
    # print(list_dict_cat_pages)

    return(list_dict_cat_pages)


if __name__ == '__main__':
    make_list_of_dict_for_all_cat_all_pages()
