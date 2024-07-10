import pytest

from survivant import Survivant
from carte import Carte
from ressource import Ressource
from zombie import Zombie

def test_avancer(self):
    survivant = Survivant(5, 5, 'nord', 100)
    survivant.avancer()
    self.assertEqual((survivant.x, survivant.y), (5, 4))

def test_tourner_a_gauche(self):
    survivant = Survivant(5, 5, 'nord', 100)
    survivant.tourner_a_gauche()
    self.assertEqual(survivant.orientation, 'ouest')

def test_tourner_a_droite(self):
    survivant = Survivant(5, 5, 'nord', 100)
    survivant.tourner_a_droite()
    self.assertEqual(survivant.orientation, 'est')

def test_ajouter_ressource(self):
    carte = Carte(10, 10)
    ressource = Ressource('nourriture')
    carte.ajouter_ressource(3, 3, ressource)
    self.assertIn((3, 3), carte.ressources)
    self.assertEqual(carte.ressources[(3, 3)], ressource)

def test_ajouter_zombie(self):
    carte = Carte(10, 10)
    zombie = Zombie(2, 2)
    carte.ajouter_zombie(zombie)
    self.assertIn(zombie, carte.zombies)