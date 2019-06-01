"""

				PROJET INFORMATIQUE - ENSTA BRETAGNE
								FISE 2021

				  ©Raphaël CHARRON & Maxime VINSOT



	Jeu de domino - classe Partie

Cette classe contient les méthodes qui vont permettre de jouer une partie de domino.

"""

# Importation des classes
from Domino import Domino
from MainJoueur import Main
from Pioche import Pioche
from Plateau import Plateau
import random



def distribution_dominos(nb_joueurs):
	""" Cette fonction va créer l'ensemble des joueurs avec le nombre nb_joueurs, cette fonction va ensuite créer
	l'ensemble des mains de chaque joueurs de façon aléatoire en fonction toujours de nb_joueurs. Puis cette fonction va
	aussi concevoir la pioche en faisant appel à la classe Pioche. """

	ensemble_des_dominos = []
	ensemble_mains = []

	# On crée l'ensemble des dominos de la partie de 28 dominos
	for i in range(6, -1, -1):
		for j in range(i, -1, -1):
			ensemble_des_dominos.append(Domino(i, j))
	random.shuffle(ensemble_des_dominos)
	# On définit le nombre de dominos dans chaque main
	if nb_joueurs == 2:
		nombre_dominos_distribue = 7
	else:
		nombre_dominos_distribue = 6
	# On crée les mains et la pioche
	for i in range(nb_joueurs):
		ensemble_mains.append(Main(ensemble_des_dominos[i * nombre_dominos_distribue:(i + 1) * nombre_dominos_distribue]))
	pioche = Pioche(ensemble_des_dominos[nombre_dominos_distribue * nb_joueurs:])
	return (ensemble_mains, pioche)



class Partie:
	""" La classe partie permet ici de définit l'ensemble des méthodes qui vont permettre de dérouler l'ensemble d'une
	partie de domino. """


	def __init__(self, plateau,main,pioche):
		self.plateau = plateau
		self.mains = main
		self.tour = None
		self.passe = 0
		self.gagnant = None
		self.pioche = pioche


	@classmethod
	def nouvelle_partie(cls,nb_joueurs):
		""" Méthode qui va créer une nouvelle partie de jeu. On va alors définir un plateau de jeu, une pioche, la partie,
		et enfin créer les mains des joueurs. """
		plateau = Plateau()
		mains,pioche = distribution_dominos(nb_joueurs)
		partie = cls(plateau,mains,pioche)
		return(partie)


########################################################################################################################
##                                  METHODES POUR LE DEBUT DE LA PARTIE                                               ##
########################################################################################################################

	@staticmethod
	def affichage_instructions():
		""" La méthode statique affichage_instructions va afficher les instructions du jeu, c'est-à-dire les règles du
		jeu pour une partie de domino. """

		print("\nDébut de la partie de domino:\n\n\
	    Le jeu peut être joué par 2 ou 4 joueurs. Grâce à un ensemble de 28 dominos, chaque joueur a une main de dominos\n\
	    qui est formée au hasard. Pour une partie à 2 joueurs, chaque joueur a 7 dominos. Pour une partie à 4 joueurs, chaque\n\
	    joueur a 6 dominos.\n\
	    Le premier à commencer la partie de domino est le joueur qui possède le domino le plus fort. Il doit alors déposer ce même\n\
	    domino sur le plateau au début de la partie. Puis chaque joueur joue à tour de rôle. Si jamais un des joueurs ne peut pas \n\
	    poser un domino sur le plateau il doit alors tirer un domino dans la pioche jusqu'à ce qu'il puisse joueur ou que la pioche\n\
	    soit vide.Si la pioche est vide, le joueur doit passer son tour, et pourra jouer au tour suivant.\n\n "
		"La partie se termine dans deux conditions :\n\
	    \t1. Si un joueur a déposé tous ses dominos et a vidé sa main. Ce joueur est le gagnant.\n\
	    \t2. Si aucun joueur ne peut jouer un domino, la partie\n\
	    \t   est arrêtée. Le joueur à qui a le moins de dominos dans sa main est le gagant.")


	def affiche_etat_mains(self):
		""" Cette méthode va afficher les informations sur les mains des joueurs. On va afficher le nombre de dominos et
		les dominos dans les mains de chaque joueurs."""
		for i in range(len(self.mains)):
			print("\nJoueur " + str(i + 1))
			print('Nombre de dominos: ' + str(len(self.mains[i])))
			print("Nombre de dominos dans la pioche: {}".format(len(self.pioche)))


	def affiche_informations_debut_tour(self):
		"""Méthode qui va afficher les informations utiles à chaque début de tour."""
		print("\nTour du joueur {}".format(self.tour+1))    # On affiche le joueur qui doit jouer
		self.affiche_etat_mains()                           # On affiche la main du joueur
		print("\nPlateau: {}".format(self.plateau))         # On affiche le plateau de jeu


	@property
	def premier_joueur(self):
		""" La méthode premier_joueur va déterminer qui est le premier joueur qui commence la partie. Pour cela elle
		détermine qui possède le plus grand domino. """
		numero_joueur = 0
		domino = Domino(0,0)
		for i in range(len(self.mains)):        # On parcours l'ensemble des mains
			if max(self.mains[i]) > domino:     # On compare les dominos un à un entre eux à l'aide des méthodes de comparaisons définient dans la classe Domino
				numero_joueur = i
				domino = max(self.mains[i])
		return(numero_joueur,domino)            # On renvoie le domino max et le joueur qui le possède


	def tour_du_premier_joueur(self):
		""" Méthode qui va réalisé les étapes du tour du premier joueur, en utilisant les méthodes précédentes. Dans cette
		méthode on va jouer le domino du premier joueur sur le plateau. """
		joueur,domino = self.premier_joueur     # On récupère le premier joueur et son premier domino
		self.tour = joueur
		print("\nLe joueur {} commence avec le domino {}.".format(joueur+1,domino))
		self.plateau.ajouter(domino,False)      # On place le domino sur le plateau sans problème de côté
		self.mains[joueur].jouer(domino)        # On joue le domino
		self.passer_prochain_joueur()           # On passe au joueur suivant


########################################################################################################################
##                                  METHODES POUR LA POSITION DU DOMINO                                               ##
########################################################################################################################

	def domino_peut_etre_joue(self,domino):
		""" Cette méthode va vérifier si le domino que le joueur veut jouer peut être poser sur le plateau en analysant
		les demi-dominos qui sont posés sur le plateau. """
		return(self.plateau.droite() in domino.liste_valeurs() or self.plateau.gauche() in domino.liste_valeurs())


	def jouer_gauche_ou_droite(self,domino):
		""" Cette méthode sera utilisé si un domino peut être jouer des deux cotés du plateau, on demande alors à l'utilisateur
		s'il veut jouer le domino à gauche ou à droite du plateau. """
		cote = input("\nDe quel côté voulez-vous le domino?\n1. Gauche\n2. Droite\nRéponse : ")     # On demande à l'utilisateur quel côté il veut jouer
		while cote not in ['1', '2']:                                                               # L'utilisateur doit répondre 1 ou 2 sinon il recommence sa réponse
			print("\nChoix non valide. Recommencez.")
			cote = input('1. Gauche\n2. Droite\n Réponse : ')
		if cote == '1':
			self.jouer_gauche(domino)                                                               # On joue le domino à gauche
		else:
			self.jouer_droite(domino)                                                               # On joue le domino à droite


	def jouer_gauche(self, domino):
		""" Méthode qui va permetre au joueur de jouer son domino sur le cote gauche du plateau. """
		print("\nLe joueur {} joue le domino {} à gauche du plateau.".format(self.tour + 1, domino))
		self.plateau.ajouter(domino,True)       # On utilise la méthode de la classe Plateau pour ajouter le domino sur le plateau
		self.mains[self.tour].jouer(domino)     # On fait appel à la méthode de jeu pour continuer la partie une fois le domino posé

	def jouer_droite(self, domino_a_jouer):
		""" Méthode qui va permetre au joueur de jouer son domino sur le cote droit du plateau. """
		print("\nLe joueur {} joue le domino {} à droite du plateau.".format(self.tour + 1, domino_a_jouer))
		self.plateau.ajouter(domino_a_jouer,False)      # On utilise la méthode de la classe Plateau pour ajouter le domino sur la partie droite du plateau
		self.mains[self.tour].jouer(domino_a_jouer)     # On fait appel à la méthode jouer pour continuer la partie une fois le domino posé


########################################################################################################################
##                                  METHODES POUR L'ENCHAINEMENT DES JOUEURS                                          ##
########################################################################################################################

	def passer_prochain_joueur(self):
		"""Méthode qui va faire passer le jeu au joueur suivant."""
		if self.tour == len(self.mains)-1:
			self.tour = 0
		else:
			self.tour += 1


	def faire_passer_joueur(self):
		"""Méthode qui va faire qu'un joueur peut passer son tour. Pour cela, on va tout d'abord lui faire piocher des
		dominos jusqu'à ce que la pioche soit vide"""
		while not self.joueur_joue_ou_passe:      # Boucle se basant sur la méthode suivante qui renvoie un booléen qui permet de sortir de la boucle
			if len(self.pioche):        # On vérifie si la pioche est vide
				print("\nLe joueur {} ne peut pas jouer. Il doit tirer un domino dans la pioche.".format(self.tour+1))
				domino = self.pioche.piocher()          # Le joueur pioche un domino
				print("\nLe joueur {} prend le domino {} dans la pioche et l'ajoute à sa main.".format(self.tour + 1,domino))
				self.mains[self.tour].ajout_domino_a_la_main(domino)        # On ajoute le domino piocher à la main du joueur
			else:
				print("\nLa pioche est vide, et le joueur {} ne peut pas jouer. Il doit passer son tour.".format(self.tour + 1))
				self.passe += 1     # Le joueur passe son tour
				break               # On sort de la boucle while
		if self.joueur_joue_ou_passe:
			print("\nLe joueur {} peut jouer.".format(self.tour+1))
			self.jouer_un_domino()  # Le joueur joue son domino


	def joueur_joue_ou_passe(self):
		""" Cette méthode va permettre de déterminer si un joueur peut jouer un domino en analysant les dominos de sa main
		et les dominos sur le plateau de jeu. Elle renvoie un booléen en fonction de la possibilité ou non de jouer un
		domino. """
		for domino in self.mains[self.tour]:            # On parcours l'ensemble des dominos de la main
			if self.domino_peut_etre_joue(domino):      # On vérifie qu'au moins un domino est jouable
				return(True)                            # On peut jouer au moins un domino
		return(False)                                   # On ne peut pas jouer de domino


	def tour_du_prochain_joueur(self):
		""" Méthode qui va exécuter l'ensemble d'un tour d'un joueur, sauf celui du premier joueur."""
		self.affiche_informations_debut_tour()      # On affiche les informations pour chaque tour par joueur
		peut_jouer = False                          # Initialisation de la variable pour savoir si le joueur va devoir passer son tour
		for domino in self.mains[self.tour]:        # Parcours des dominos dans la main du joueur
			# On teste si un demi-domino de la main du joueur est égale à une des valeurs aux extrémités du plateau
			if self.plateau.gauche() in domino.liste_valeurs() or self.plateau.droite() in domino.liste_valeurs():
				peut_jouer = True
				break
		if peut_jouer:                              # Le joueur joue
			self.passe = 0
			self.jouer_un_domino()
			self.verifie_gagnant()
		else:                                       # Le joueur passe son tour
			self.faire_passer_joueur()
		self.passer_prochain_joueur()               # Changement de joueur


########################################################################################################################
##                                  METHODES POUR JOUER UN DOMINO                                                     ##
########################################################################################################################

	def demander_numero_domino_a_jouer(self):
		""" Cette méthode va permettre de faire la demande en console au joueur de choisir le domino qu'il veut poser sur
		le plateau de jeu. On vérifir ensuite si le choix est valable ou non. """
		print("\nMain du joueur {}:".format(self.tour+1))               # On affiche la main du joueur
		print(self.mains[self.tour])
		choix = input("\nQuel domino choisissez vous jouer?")           # On demande au joueur de choisir le domino qu'il veut jouer
		while not (choix.isnumeric() and int(choix) in range(1,len(self.mains[self.tour])+1)):  # Vérification si le choix est correct
			print("\nLe choix est incorrecte. Veuillez recommencer.")
			choix = input("Quel domino shouaitez-vous jouer?")
		choix = int(choix)-1                                            # On retire 1 car les dominos sont stockés dans une liste python commencant à 0
		return(self.mains[self.tour][choix])                            # On renvoie le domino choisi


	def jouer_un_domino(self):
		""" Méthode qui va permettre de joueur un domino, pour cela on va tester les dominos sur le plateau et demander
		le choix de domino à l'utilisateur. Puis on va essayer de placer le domino sur le plateau automatiquement. """
		domino_a_jouer = self.demander_numero_domino_a_jouer()
		# On vérifie s'il est possible de jouer le domino sur le plateau
		while self.plateau.gauche() not in domino_a_jouer.liste_valeurs() and self.plateau.droite() not in domino_a_jouer.liste_valeurs():
			print("\nCe domino ne peut pas être joué pour l'instant.")
			print("\nPlateau: {}".format(self.plateau))
			domino_a_jouer = self.demander_numero_domino_a_jouer()
		# Jouable des deux côtés
		if self.plateau.gauche() in domino_a_jouer.liste_valeurs() and self.plateau.droite() in domino_a_jouer.liste_valeurs():
			self.jouer_gauche_ou_droite(domino_a_jouer)        # On demande à présent à l'utilisateur quel côté il choisit
		# Jouable à gauche
		elif self.plateau.gauche() in domino_a_jouer.liste_valeurs():
			self.jouer_gauche(domino_a_jouer)
		# Jouable à droite
		else:
			self.jouer_droite(domino_a_jouer)


########################################################################################################################
##                                  METHODES POUR LA FIN D'UNE PARTIE                                                 ##
########################################################################################################################

	def verifie_gagnant(self):
		""" Cette méthode va vérifier si le joueur actuel à gagner la partie, càd on va vérifier si sa main est vide."""
		if not len(self.mains[self.tour]):  # On vérifie si la main du joueur est vide
			self.gagnant = self.tour+1


	def joueurs_avec_moins_de_dominos(self):
		""" Cette méthode va parcourir l'ensemble des domino de chaque joueur et regarder celui qui a le plus petit nombre
		de domino en main. Ce joueur sera déclaré gagnant en cas d'égalité. """
		longueur_minimum_main = 15                              # On définit une taille minimale de main, on prend 15 au hasard cela aurait pu être plus ou moins. En faisant attention à ne pas prendre un chiffre trop petit
		gagnant = []
		for i in range(len(self.mains)):                        # On parcourt les mains
			if len(self.mains[i]) < longueur_minimum_main:
				longueur_minimum_main = len(self.mains[i])
				gagnant = [i+1]
			elif len(self.mains[i]) == longueur_minimum_main:        # On arrive à un minimum
				gagnant.append(i+1)
		return(gagnant)


	def egalite(self,indice):
		""" Cette méthode va simplement renvoyé un message en console si jamais deux joueurs sont à égalité à la fin de
		la partie. """
		print('\nIl y a une égalité entre plusieurs joueurs. Les gagnants sont :', end=' ')
		for i in range(len(indice)):    # On parcourt l'ensemble des joueurs à égalité
			if i == len(indice)-1:
				print('et {}!'.format(indice[i]))
			else:
				print('{},'.format(indice[i]), end=' ')


	def victoire(self):
		""" Cette méthode va afficher un message de victoire, si un joueur gagne la partie de domino."""
		print("\nLe joueur {} n'a plus de domino. Il gagne la partie!".format(self.gagnant))


########################################################################################################################
##                                  METHODES POUR JOUER LA PARTIE                                                     ##
########################################################################################################################

	def jouer(self):
		""" C'est la méthode principale, elle gère le déroulement complet d'une partie de domino."""
		self.affichage_instructions()                                     # On affiche les règles du jeu
		self.tour_du_premier_joueur()                                   # On fait jouer le premier joueur
		while self.gagnant is None:                                     # On parcours tant qu'il n'y a pas de gagnant
			self.tour_du_prochain_joueur()                              # Joueur suivant joue
			if self.passe == len(self.mains):                           # Lorsque la pioche est vide on cherche un gagnant
				self.gagnant = self.joueurs_avec_moins_de_dominos()
		if isinstance(self.gagnant,int) or len(self.gagnant) == 1:      # On vérifie que l'on a un gagnant
			if not isinstance(self.gagnant,int):
				self.gagnant = self.gagnant[0]
			self.victoire()                                             # Affiche le message de victoire
		else:
			self.egalite(self.gagnant)                                  # Affiche le message en cas d'égalité




########################################################################################################################
#												Jeu contre l'IA                                                        #
########################################################################################################################
	#
	# def IA_basique(self):
	# 	'''Méthode qui permet de créer une intelligente artificielle simple qui pose un domino seule.'''
	#
	# 	# domino_a_jouer = self.demander_numero_domino_a_jouer()
	# 	# On récupère les valeurs aux extrémités du plateau
	# 	domino_a_gauche = self.plateau.gauche()
	# 	domino_a_droite = self.plateau.droite()
	# 	joue = True
	# 	a_jouer = False
	#
	# 	while a_jouer == False:
	# 		for domino in self.mains[self.tour]:
	# 			if domino_a_gauche in domino.liste_valeurs():  # L'IA peut jouer à gauche
	# 				self.jouer_gauche(domino)
	#
	# 				a_jouer = True
	#
	# 			elif domino_a_droite() in domino.liste_valeurs():  # L'IA peut jouer à droite
	# 				self.jouer_droite(domino)
	# 				a_jouer = True
	#
	# 			joue = False
	#
	# 	if joue == False:
	# 		if len(self.pioche):  # On vérifie si la pioche est vide
	# 			print("\nLe joueur {} ne peut pas jouer. Il doit tirer un domino dans la pioche.".format(self.tour+1))
	# 			domino = self.pioche.piocher()
	# 			print(
	# 				"\nLe joueur {} prend le domino {} dans la pioche et l'ajoute à sa main.".format(self.tour+1,domino))
	# 			self.mains[self.tour].ajout_domino_a_la_main(domino)
	#
	# 		else:
	# 			print("\nLa pioche est vide, et le joueur {} ne peut pas jouer. Il doit passer son tour.".format(self.tour + 1))
	# 			self.passe += 1
	# 			#break
	#
	# def tour_du_prochain_joueur_IA(self):
	# 	""" Méthode qui va exécuter l'ensemble d'un tour d'un joueur, sauf celui du premier joueur."""
	#
	# 	self.affiche_informations_debut_tour()      # On affiche les informations pour chaque tour par joueur
	# 	peut_jouer = False                          # Initialisation de la variable pour savoir si le joueur va devoir passer son tour
	#
	# 	for domino in self.mains[self.tour]:        # Parcours des dominos dans la main du joueur
	# 		# On teste si un demi-domino de la main du joueur est égale à une des valeurs aux extrémités du plateau
	# 		if self.plateau.gauche() in domino.liste_valeurs() or self.plateau.droite() in domino.liste_valeurs():
	# 			peut_jouer = True
	# 			break
	#
	# 	if peut_jouer:                              # Le joueur joue
	# 		self.passe = 0
	# 		self.jouer_un_domino()
	# 		self.verifie_gagnant()
	#
	# 	else:                                       # Le joueur passe son tour
	# 		#self.joueur_passe_son_tour()
	# 		self.faire_passer_joueur()
	# 	self.passer_prochain_joueur()               # Changement de joueur
	#
	#
	# def jouerIA(self):
	# 	""" C'est la méthode principale, elle gère le déroulement complet d'une partie de domino."""
	#
	# 	self.affiche_instructions()                                     # On affiche les règles du jeu
	# 	self.tour_du_premier_joueur()                                   # On fait jouer le premier joueur
	#
	# 	while self.gagnant is None:                                     # On parcours tant qu'il n'y a pas de gagnant
	# 		self.tour_du_prochain_joueur()                              # Joueur suivant joue
	#
	# 		if self.passe == len(self.mains):                           # Lorsque la pioche est vide on cherche un gagnant
	# 			self.gagnant = self.joueurs_avec_moins_de_dominos()
	#
	# 	if isinstance(self.gagnant,int) or len(self.gagnant) == 1:      # On vérifie que l'on a un gagnant
	# 		if not isinstance(self.gagnant,int):
	# 			self.gagnant = self.gagnant[0]
	#
	# 		self.victoire()                                             # Affiche le message de victoire
	#
	# 	else:
	# 		self.egalite(self.gagnant)                                  # Affiche le message en cas d'égalité
