from classTomatoBush import TomatoBush
from classTomato import Tomato


class Garden:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:
            print('not ripe')

    @staticmethod
    def knowledge_base():
        print('base')





