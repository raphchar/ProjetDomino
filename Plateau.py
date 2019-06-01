"""

                PROJET INFORMATIQUE - ENSTA BRETAGNE
                                FISE 2021

                  ©Raphaël CHARRON & Maxime VINSOT



    Jeu de domino - classe Plateau

Cette classe contient les méthodes qui vont permettre de définir le plateau de jeu pour une partie de domino.

"""



class Plateau:
    """Cette classe plateau va être utilisée pour définir la surface de jeu pour la partie de domino. On va aussi définir
    des méthodes dans cette classe permettant de gérer la posibilité de joué un domino ou non."""

    def __init__(self):
        self.plateau = []

########################################################################################################################
##                                  METHODES DE REPRESENTATION DES MAINS                                              ##
########################################################################################################################

    def gauche(self):
        """ Cette méthode renvoie la valeur du demi-domino à l'extrémité gauche du plateau."""
        return(self.plateau[0].chiffre1)


    def droite(self):
        """ Cette méthode renvoie la valeur du demi-domino à l'extrémité droite du plateau."""
        return(self.plateau[-1].chiffre2)


########################################################################################################################
##                                  METHODES POUR AJOUTER DES DOMINOS SUR LE PLATEAU                                  ##
########################################################################################################################

    def ajouter_gauche(self,domino):
        """ Cette méthode va ajouter un domino sur la partie gauche du plateau. """
        if self.gauche() == domino.chiffre1:
            self.plateau.insert(0,domino.inverse())
        else:
            self.plateau.insert(0,domino)


    def ajouter_droite(self, domino):
        """ Cette méthode va ajouter un domino sur la partie droite du plateau. """
        if self.droite() == domino.chiffre1:
            self.plateau.append(domino)
        else:
            self.plateau.append(domino.inverse())


    def ajouter(self,domino,position):
        """ Cette méthode va ajouter un domino sur un des côtés du plateau en fonction des bords du plateau et du domino
        à jouer. """
        if not self.plateau:  # Si le plateau est vide
            self.plateau.insert(0,domino)
        else:
            if position:
                self.ajouter_gauche(domino)
            else:
                self.ajouter_droite(domino)


########################################################################################################################
##                                  METHODES DE REPRESENTATION DU PLATEAU                                             ##
########################################################################################################################

    # def __eq__(self,other):
    #     if not isinstance(other, type(self)):
    #         return False
    #     return self.__dict__ == other.__dict__

    # def __ne__(self, other):
    #     return not self == other


    def __len__(self):
        """ La méthode __len__ renvoie la taille du plateau, c'est-à-dire le nombre dominos qui ont été posé sur le
        plateau de jeu. """
        return len(self.plateau)


    def __str__(self):
        """ Cette méthode va renvoyer une représentation du plateau avec les domino."""
        les_dominos_plateau = ' '
        for domino in self.plateau:
            les_dominos_plateau += str(domino)
        return(les_dominos_plateau)


    def __repr__(self):
        """ Cette méthode renvoie la représentation du plateau à l'aide de la méthode __str__."""
        return str(self)
