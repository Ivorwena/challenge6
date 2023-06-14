import os
from pathlib import Path
from os import system
import shutil


def greet():
    system('clear')
    name = input("Tell me your name: ")
    print(f"Welcome {name}. The recipes are in home/administrator directory, main folder is called 'Recipes'.")
    num = count_recipes()
    print(f"There are total {num} recipes.")


def option():
    print("Choose one of the options:\n"
          "[1] - read recipe\n"
          "[2] - create recipe\n"
          "[3] - create category\n"
          "[4] - delete recipe\n"
          "[5] - delete category\n"
          "[6] - end program")
    number = input("Make your choice: ")
    possibilities = ['1', '2', '3', '4', '5', '6']
    if number not in possibilities:
        while number not in possibilities:
            print("That is not one of the options.")
            number = input("Make your choice: ")
    number = int(number)
    return number


def count_recipes():
    os.chdir('/home/administrator/Recipes')
    file_counter = 0
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.txt'):
                file_counter += 1
    return file_counter


def choose(number):
    if number == 1:
        print("read_recipe")
        choose_dir(".")
        choose_rec()
    elif number == 2:
        print("create_recipe")
        choose_dir(".")
        create_rec()
    elif number == 3:
        print("create_category")
        create_cat()
    elif number == 4:
        print("delete_recipe")
        choose_dir(".")
        del_rec()
    elif number == 5:
        print("delete_category")
        del_cat()
    else:
        print("Thanks for cooperation")
        return 0


def print_dir():
    folders = os.listdir(".")
    print(folders)
    return folders


def choose_dir(base):
    print("\nHere are possible categories - choose one of them by writing it's name.")
    print("Don't make mistake in the name - remember about capital letters.\n")
    direct = print_dir()
    where_to_go = input("Choose category: ")
    if where_to_go not in direct:
        while where_to_go not in direct:
            print("\nThere ain't such category - try again.\n")
            print(direct)
            where_to_go = input("Choose category: ")
    guide = Path(base, where_to_go)
#    print(guide)
    os.chdir(guide)


def show_rec():
    rec = os.listdir(".")
    print(rec)
    return rec


def choose_rec():
    print("\nHere are possible recipes - choose one of them by writing it's name.")
    print("Don't make mistake in the name - remember about capital letters and file extension.\n")
    direct = show_rec()
    where_to_go = input("Choose recipe: ")
    if where_to_go not in direct:
        while where_to_go not in direct:
            print("\nThere ain't such file - try again.\n")
            print(direct)
            where_to_go = input("Choose recipe: ")
    recipe = open(where_to_go)
    whole = recipe.readlines()
    print(whole)


def create_rec():
    alfabet = "abcdefghijklmnoprstquvxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
    name = input("Give me the name of your recipe (without extension): ")
    if name == "" or name[0] not in alfabet:
        while name == "" or name[0] not in alfabet:
            print("Wrong name")
            name = input("Give me the name of your recipe (without extension): ")
    ext = ".txt"
    new_name = name + ext
    file = open(new_name, 'w')
    content = input("Write the recipe. When you finish - press enter.\n")
    file.write(content)
    file.close()


def create_cat():
    alfabet = "abcdefghijklmnoprstquvxyzABCDEFGHIJKLMNOPRSTUVWXYZ"
    name = input("Give me the name of the new category: ")
    if name == "" or name[0] not in alfabet:
        while name == "" or name[0] not in alfabet:
            print("Wrong name")
            name = input("Give me the name of the new category: ")
    guide = Path('/home/administrator/Recipes', name)
    os.mkdir(guide)


def del_rec():
    print("\nHere are possible recipes - choose one of them by writing it's name.")
    print("Don't make mistake in the name - remember about capital letters and file extension.\n")
    direct = show_rec()
    name = input("Which file do you want to delete? You can stop process by writing 'none'. ")
    if name not in direct:
        while name not in direct:
            if name == "none":
                return 0
            print("\nThere ain't such file - try again.\n")
            print(direct)
            name = input("Choose file: ")
    os.remove(name)


def del_cat():
    print("\nHere are possible categories - choose one of them by writing it's name.")
    print("Don't make mistake in the name - remember about capital letters.\n")
    direct = print_dir()
    name = input("Which category do you want to delete? You can stop process by writing 'none'. ")
    if name not in direct:
        while name not in direct:
            if name == "none":
                return 0
            print("\nThere ain't such category - try again.\n")
            print(direct)
            name = input("Choose category: ")
    shutil.rmtree(name)


wrap = 0
while wrap != 6:
    greet()
    choice = option()
    choose(choice)
    input("Press ENTER to continue...")
    wrap = choice
