"""
Programming 1 Practical 7
"""

from prac_07.guitar_attributes import Guitar


def main():
    i = 0
    my_guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Another Guitar", 2012, 1000)]
    while True:
        new_guitar_name = input("Name: ")
        if new_guitar_name == "":
            break
        new_guitar_year = int(input("Year: "))
        if new_guitar_year == "":
            break
        new_guitar_price = int(input("Price: "))
        if new_guitar_price == "":
            break
        print(Guitar(new_guitar_name, new_guitar_year, new_guitar_price), "added.")
        my_guitars.append(Guitar(new_guitar_name, new_guitar_year, new_guitar_price))
    for guitar in my_guitars:
        if guitar.is_vintage():
            vintage_string = ""
        else:
            vintage_string = "vintage"
        print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                   vintage_string))
        i += 1


main()
