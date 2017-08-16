"""
CP1404/CP5632 - Practical - Suggested Solution
Get a valid name and display parts of it
"""


def version_1():
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")

    print(name[::2])


def main():
    name = get_name()
    print_parts(name, 3)


def print_parts(name, step=2):
    print(name[::step])


def get_name():
    name = input("Name: ")
    while name == "":
        print("Invalid name.")
        name = input("Name: ")
    return name


main()