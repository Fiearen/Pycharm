"""
Programming 1 Practical 7
"""

from prac_07.guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1922,  16035.40)
second_guitar = Guitar("Another Guitar", 2012,  1000)

print("Gibson L-5 CES  get_age() - Expected 95. Got", first_guitar.get_age())
print("Another Guitar get_age() - Expected 5. Got", second_guitar.get_age())

print("\nGibson L-5 CES  is_vintage() - Expected True. Got", first_guitar.is_vintage())
print("Another Guitar is_vintage() - Expected False. Got", second_guitar.is_vintage())
