class Carte:
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.ressources = {}
        self.zombies = []

    def ajouter_ressource(self, x, y, ressource):
        self.ressources[(x, y)] = ressource

    def ajouter_zombie(self, zombie):
        self.zombies.append(zombie)
