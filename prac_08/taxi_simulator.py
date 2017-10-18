"""
Programming 1 - Practical 7
Do From Scratch Exercise- Taxi Simulator
"""
from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    choice = input("Let's drive!\nq)uit, c)hoose taxi, d)rive\n>>>").upper()
    taxi = ""
    total_fair = 0
    while choice != "Q":
        if choice == "C":
            taxi = choose_taxi(taxis)
        elif choice == "D":
            if taxi == "":
                print("Please choose a taxi.")
                taxi = choose_taxi(taxis)
            else:
                distance_to_drive = int(input("Drive how far? "))
                taxi.drive(distance_to_drive)
                total_fair += taxi.get_fare()
                print(taxi)
                print(total_fair)
                taxi.start_fare()
        else:
            print("Invalid Choice")
        choice = input("q)uit, c)hoose taxi, d)rive\n>>>").upper()


def choose_taxi(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))
    chosen_taxi = int(input("Choose taxi: "))
    chosen_taxi = taxis[chosen_taxi]
    print("Bill to date: {}".format(chosen_taxi.get_fare()))
    return chosen_taxi

main()
