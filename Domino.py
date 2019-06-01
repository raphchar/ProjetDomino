"""

                PROJET INFORMATIQUE - ENSTA BRETAGNE
                                FISE 2021

                  ©Raphaël CHARRON & Maxime VINSOT



    Jeu de domino - classe Partie

Cette classe contient les méthodes qui vont permettre de définir un domino pour une partie de domino.

"""


class Domino:
    """
    Dominos qui seront joués. Chaque domino a deux chiffres, et chaque assortiment de chiffres est unique.
    Par exemple, on ne peut pas avoir le domino [6|6] dans deux donnes.
    Attributs:
        premier_chiffre (int): Premier chiffre du domino (entier entre 0 et 6)
        deuxiement_chiffre (int): Deuxieme chiffre du domino (entier entre 0 et 6)
    """


    def __init__(self,valeur1,valeur2):
        self.chiffre1 = valeur1             # On définit les valeurs des demi-dominos
        self.chiffre2 = valeur2


########################################################################################################################
##                                  METHODES DE REPRESENTATION DES DOMINOS                                            ##
########################################################################################################################

    def __str__(self):
        """ La méthode __str__ va permettre de renvoyer le domino sous la forme d'une chaîne de caractère. """
        return "[{}|{}]".format(self.chiffre1,self.chiffre2)


    def __repr__(self):
        """ La méthode __repr__ va permettre d'utiliser la méthode str et de renvoyer ainsi à l'utilisateur la
         représentation du domino. """
        return str(self)


    def inverse(self):
        """ La méthode inverse va renvoyer le domino ayant les valeurs de ses demi-dominos inversés. """
        return Domino(self.chiffre2, self.chiffre1)


########################################################################################################################
##                                  METHODES DE TESTS SUR LES DOMINOS                                                 ##
########################################################################################################################

    def __eq__(self,domino):
        """ Méthode qui va effectuer un test d'équivalence entre deux dominos."""
        if not isinstance(domino,type(self)):
            return False
        else:
            return sorted((self.chiffre1,self.chiffre2)) == sorted((domino.chiffre1,domino.chiffre2))


    def __gt__(self,domino):
        """ Cette méthode permet de réaliser un test de comparaison entre deux dominos. Pour cela on commence par tester
        la différence entre la somme des chiffres du domino puis on s'intéresse au demi-domino. """
        if not isinstance(domino,type(self)):
            return False
        if self.somme_chiffres() == domino.somme_chiffres():
            return self.chiffre1 > domino.chiffre1
        else:
            return self.somme_chiffres() > domino.somme_chiffres()


    # def __hash__(self):
    #     """
    #     Cette méthode spécifie la fonction de hachage pour les objets de la classe domino. Ceci permet de créer des
    #     ensembles d'objets de cette classe
    #     """
    #     return(hash(tuple(sorted((self.chiffre1,self.chiffre2)))))


    # def __contains__(self,clé):
    #     """
    #     Cette méthode spécifie le test d'appartenance pour un entier dans un objet de la classe domino
    #     :param key (int): Chiffre dont on vérifier l'appartenance dans l'objet domino
    #     :return (bool): True si le chiffre key est présent dans les attributs du domino, False autrement
    #     """
    #     return(clé == self.chiffre1 or clé == self.chiffre2)


########################################################################################################################
##                                  METHODES DE UTILES POUR UNE PARTIE DE DOMINO                                      ##
########################################################################################################################


    def somme_chiffres(self):
        """ La méthode somme_chiffres permet de calculer la somme des demi-dominos d'un domino. Utile pour le début de
        la partie, pour savoir quel joueur commence la partie. """
        return self.chiffre1 + self.chiffre2


    def liste_valeurs(self):
        """ Cette méthode va permettre de mettre sous forme d'une liste les valeurs des demi-dominos. """
        return [self.chiffre1, self.chiffre2]
