from Script_scrap_one_book import save_one_book
from Script_scrap_one_category import save_one_category
from Script_scrap_all_categories import save_all_categories
from defTEST_create_path_and_repertory import create_path_and_repertory


def main():

    script = False
    while script is False:
        which_script = input("This program contains three different scripts:\n \
        1: for a book \n \
        2: for a book category \n \
        3: for all categories of books\n \
        For use a script enter correct number : ")

        if which_script is '1':
            save_one_book()
            script = True
        elif which_script is '2':
            save_one_category()
            script = True
        elif which_script is '3':
            save_all_categories()
            script = True
        else:
            script = False


if __name__ == '__main__':
    main()
