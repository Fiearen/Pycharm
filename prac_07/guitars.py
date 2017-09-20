"""
Programming 1 Practical 7
"""

from prac_07.guitar_attributes import Guitar
def main():
    my_guitars = [Guitar("Gibson L-5 CES", 1922,  "$16,035.40"), Guitar("Another Guitar", 2012,  "$1000")]
    while True:
        new_guitar_name = input("Name: ")
        if new_guitar_name == "":
            break
        new_guitar_year = input("Year: ")
        if new_guitar_year == "":
            break
        new_guitar_price = input("Price: ")
        if new_guitar_price == "":
            break
        print(Guitar(new_guitar_name, new_guitar_year, new_guitar_price), "added.")
        my_guitars.append(Guitar(new_guitar_name, new_guitar_year, new_guitar_price))
    for guitar in my_guitars:
        print("These are my Guitars:", my_guitars)


main()
