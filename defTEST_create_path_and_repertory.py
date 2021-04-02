#from constants import REPERTORY_NAME
import os


def create_path_and_repertory():

    print("To use this program you must indicate to which directory the information will be copied.")

    path_repertory = input("Enter the path where the file and folder will be copied : ")

    path_repertory_bool = False
    while path_repertory_bool is False:
        try:
            os.chdir(path_repertory)
            path_repertory
            path_repertory_bool = True
        except FileNotFoundError:
            print("The specified path was not found !!")
            path_repertory = input("Enter valid path where the folder and file will be copied : ")
            continue

    try:
        os.mkdir(REPERTORY_NAME)
    except FileExistsError:
        print("Cannot create an already existing directory")
        user_agreement = input("Do you want use this directory or a new one ? press 'y', press 'n' : ")
        if user_agreement == "y":
            pass
        else:
            REPERTORY_NAME = input("New name for directory : ")
            os.mkdir(REPERTORY_NAME)

    path = (path_repertory + '/' + REPERTORY_NAME + '/')
    print("Name of repertory : ", REPERTORY_NAME, ' at this path : ', path_repertory)
    os.chdir(REPERTORY_NAME)
