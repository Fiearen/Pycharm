
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
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            print("{:2}".format(number), end=' ')
        print()


main()
