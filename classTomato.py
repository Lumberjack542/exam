class Tomato:

    states = {0: 'first', 1: "second", 2: "last"}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        if self._state == self.states[2]:
            print("ripe tomato")
        else:
            print('not ripe')






