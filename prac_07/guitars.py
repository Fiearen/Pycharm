"""
Programming 1 Practical 7
"""

from prac_07.guitar import Guitar


def main():
    i = 0
    my_guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Another Guitar", 2012, 1000)]
    new_guitar_name = input("Name: ")
    while new_guitar_name != "":
        new_guitar_year = int(input("Year: "))
        new_guitar_price = int(input("Price: "))
        print(Guitar(new_guitar_name, new_guitar_year, new_guitar_price), "added.")
        my_guitars.append(Guitar(new_guitar_name, new_guitar_year, new_guitar_price))
        new_guitar_name = input("Name: ")
    for guitar in my_guitars:
        if guitar.is_vintage():
            vintage_string = "vintage"
        else:
            vintage_string = ""
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))
        i += 1


main()
