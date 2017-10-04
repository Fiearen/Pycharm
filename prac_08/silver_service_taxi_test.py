"""
Programming 1 - Practical 7
Intermediate Exercise - Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

silver_taxi_1 = SilverServiceTaxi("Hummer", 200, 2)
print("{} ${:.2f}".format(silver_taxi_1, silver_taxi_1.get_fare()))

silver_taxi_1.drive(18)
print("{}, ${:.2f}".format(silver_taxi_1, silver_taxi_1.get_fare()))
