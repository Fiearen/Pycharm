"""
Programming 1 -Practical 7
intermediate exercise - unreliable car test
"""

from prac_08.unreliable_car import UnreliableCar

unreliable_car_1 = UnreliableCar("Old Car", 100, 10)
for i in range(100):
    far = unreliable_car_1.drive(1)
    print(far)
    # print(unreliable_car_1)
