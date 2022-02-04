from classTomato import Tomato


class TomatoBush:

    def __init__(self, num_of_tom):
        self.tomatoes = [Tomato(index) for index in range(0, num_of_tom)]

    def grow_all(self):
        for i in self.tomatoes:
            i.grow()

    def all_are_ripe(self):
        return all([i.is_ripe() for i in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []