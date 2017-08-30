
import random

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("That doesn't make sense!")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        numbers = []
        while len(numbers) < 6:
            number = random.randint(MINIMUM, MAXIMUM)
            while number in numbers:
                number = random.randint(MINIMUM, MAXIMUM)
            numbers.append(number)
            print("{:2}".format(number), end=' ')
        print()


main()
