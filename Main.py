'''

                PROJET INFORMATIQUE - ENSTA BRETAGNE
                                FISE 2021

                  ©Raphaël CHARRON & Maxime VINSOT



    Jeu de domino - Fichier Main

Fichier Main du jeu de domino, ce fichier va lancer la partie à l'aide de la classe Partie.

'''

# Importation de la classe Partie
from Partie import Partie
from PartieIA import PartieIA


if __name__ == '__main__':
   
    print("Jouons une partie de domino!\n")

    nb_joueurs = input("\nShouaitez-vous jouer à 2 ou 4 joueurs? \n")
    while nb_joueurs not in ['2', '4']:
        nb_joueurs = input("Choix non valide. Veuillez-entrer le nombre de joueurs avec lequel vous voulez jouer.\n")
    nb_joueurs = int(nb_joueurs)



    ## Code utile si jamais on veut jouer contre l'IA en cours de construction ##

    # if nb_joueurs == 2:
    #     choix_IA = input("Souhaitez vous jouer contre une intelligence artificielle ? \n"
    #                      "1. Oui \n"
    #                      "2. Non\n"
    #                      "Votre choix : ")
    #
    #     while choix_IA not in ['1', '2']:
    #         nb_joueurs = input("Choix non valide. Veuillez-entrer une réponse correcte : \n")
    #
    #     choix_IA = int(choix_IA)
    #
    #     if choix_IA == 1:       # Jeu contre une IA
    #         partie_IA = PartieIA.nouvelle_partie_IA(nb_joueurs)
    #         partie_IA.jouerIA()
    #     else:                   # Jeu à 2 sans IA
    #         partie = Partie.nouvelle_partie(nb_joueurs)
    #         partie.jouer()
    #else:                       # Jeu à 4

    partie = Partie.nouvelle_partie(nb_joueurs)
    partie.jouer()

    input('Appuyer sur ENTER pour quitter.')
