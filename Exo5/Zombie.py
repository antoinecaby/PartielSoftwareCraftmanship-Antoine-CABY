import random

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def deplacer(self):
        mouvements = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        mouvement = random.choice(mouvements)
        self.x += mouvement[0]
        self.y += mouvement[1]