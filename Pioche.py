"""

				PROJET INFORMATIQUE - ENSTA BRETAGNE
								FISE 2021

				  ©Raphaël CHARRON & Maxime VINSOT



	Jeu de domino - classe Partie

Cette classe contient les méthodes qui vont permettre de piocher un domino dans la pioche de la partie de domino.

"""


# Importation des classes utiles
from MainJoueur import Main
from random import randint



class Pioche(Main):
	""" Définition de la classe pioche qui hérite de la classe Main (fichier Main_joueur). On va définir dans cette classe une seule méthode
	qui va permettre de piocher un domino dans la pioche lorsque le joueur ne peut pas jouer."""

	def piocher(self):
		""" Cette méthode va permettre dans la partie de domino aux joueurs de piocher un domino dans la pioche
		lorsqu'ils ne peuvent pas jouer. """
		return(self.dominos.pop(randint(0,len(self.dominos)-1)))
