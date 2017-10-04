"""
Programming 1 - Practical 7
Do From Scratch Exercise- Taxi Simulator
"""
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi

TAXIS = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    choice = input("Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>>").upper()
    taxi = ""
    while choice != "Q":
        if choice == "C":
            taxi = choose_taxi()
            print(taxi)
        elif choice == "D":
            if taxi == "":
                print("Please choose a taxi.")
            else:
                drive(taxi)
        else:
            print("Invalid Choice")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>>").upper()


def choose_taxi():
    i = 0
    for taxi in TAXIS:
        print("Taxis available:\n{} - {}".format(i, taxi))
        i += 1
    chosen_taxi = input("Choose taxi: ")
    return chosen_taxi


def drive(taxi):
    distance_to_drive = int(input("Drive how far? "))
    print("Bill to date: {}".format())

main()
