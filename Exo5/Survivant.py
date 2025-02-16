class Survivant:
    def __init__(self, x, y, orientation, sante):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.sante = sante
        self.inventaire = []

    def tourner_a_gauche(self):
        orientations = ['nord', 'ouest', 'sud', 'est']
        index = orientations.index(self.orientation)
        self.orientation = orientations[(index + 1) % 4]

    def tourner_a_droite(self):
        orientations = ['nord', 'est', 'sud', 'ouest']
        index = orientations.index(self.orientation)
        self.orientation = orientations[(index + 1) % 4]

    def avancer(self):
        if self.orientation == 'nord':
            self.y -= 1
        elif self.orientation == 'sud':
            self.y += 1
        elif self.orientation == 'est':
            self.x += 1
        elif self.orientation == 'ouest':
            self.x -= 1