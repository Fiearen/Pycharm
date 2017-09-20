"""
Programming 1 Practical 7
"""
CURRENT_YEAR = 2017

class Guitar:
    def __init__(self, name="", year=0, cost="$0"):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : {}".format(self.name, self.year, self.cost)

    def is_vintage(self):
        if 2017 - self.year >= 50:
            return True
        return False

    def get_age(self):
        return CURRENT_YEAR - self.year
