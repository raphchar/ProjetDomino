"""

                PROJET INFORMATIQUE - ENSTA BRETAGNE
                                FISE 2021

                  ©Raphaël CHARRON & Maxime VINSOT



    Jeu de domino - classe MainJoueur

Cette classe contient les méthodes qui vont permettre de définir la main de chaque joueur de la partie de domino.

"""


class Main:
    """ Classe qui va permettre de créer les mains des joueurs avec leur dominos. """

    def __init__(self,les_dominos):
        self.dominos = list(les_dominos)            # On crée un ensemble de dominos sous forme de liste


########################################################################################################################
##                                  METHODES DE REPRESENTATION DES MAINS                                              ##
########################################################################################################################

    def __getitem__(self,i):
        """ Méthode qui permet de récupérer un domino de notre liste de domino créer dans l'initialisation de la
        classe Main. """
        return self.dominos[i]                      # On sort le domino à la position i dans notre liste de domino

    # def __eq__(self,other):
    #     """ Cette méthode permet de vérifier que les types des éléments que l'on compare sont les mêmes. """
    #     if not isinstance(other,type(self)):
    #         return False
    #     return self.__dict__ == other.__dict__
    #
    # def __ne__(self,other):
    #     return not self == other

    def __len__(self):
        """ La méthide __len__ permet de renvoyer la longueur de la liste contenant les dominos. Utile pour savoir le
        nombre de dominos dans les mains et la pioche. """
        return len(self.dominos)

    def __str__(self):
        """ Cette méthode va permettre de renvoyer la liste des domino d'une main ou de la pioche sous la forme d'une
        châine de caractère. """
        ligne_domino = " "                                                  # On crée notre ligne de domino pour l'affichage
        for i in range(len(self.dominos)):                                  # Parcourt de la liste de domino
            ligne_domino += "\n{}. {}".format(i + 1, self.dominos[i])       # On ajoute 1 à 1 les domino à notre liste
        return ligne_domino

    def __repr__(self):
        """ Cette méthode permet de renvoyer la liste des dominos à l'aide de la méthode __str__ qui aura au par avant
        transformé le type de la représentation des dominos. """
        return str(self)

########################################################################################################################
##                                  METHODES QUI VONT SERVIRE PENDANT LE JEU POUR LES MAINS                           ##
########################################################################################################################

    def jouer(self,domino):
        """ La méthode joueur va permettre de jouer un domino en le retirant de la main du joueur. Pour cela on prend
        en paramètre un domino, trouver son positionnement dans notre liste puis on le retire de la liste de domino. """
        index_domino = self.dominos.index(domino)
        self.dominos.remove(domino)
        return index_domino


    def ajout_domino_a_la_main(self,domino,i=None):
        """ Cette méthode va permettre de pouvoir ajouer une domino dans la main du joueur après que celui-ci ait pioché
        par défaut nous ajouterons ce domino à la fin de sa main. """
        if i is None:
            i = len(self.dominos)
        self.dominos.insert(i,domino)


