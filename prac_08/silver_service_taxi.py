"""
Programming 1 - Practical 7
Intermediate Exercise - Silver Service Taxi
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        return super().get_fare() + self.flagfall
