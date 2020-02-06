# -*- coding: utf8 -*-

""" Fonctions pour ouvrir une grille de niveau, vérifier si une grille est gagnante et passer à l'état suivant d'une grille
Pour utiliser ces fonctions dans un programme, faire 
import fonctions_base
from fonctions_base import *
"""


def creer_grille(niveau):
    "Ouvre le fichier de niveau dont le numéro est donné en paramètre, puis renvoie la grille de jeu créée"

    f = open("grille" + str(niveau) + ".niv", "r")
    taille_grille = f.readline()
    pattern = f.readline()
    f.close()

    dimensions = taille_grille.split(" ")[:2]
    dimensions[0], dimensions[1] = int(dimensions[0]), int(dimensions[1])
    taille_grille = dimensions[0] * dimensions[1]
    grille = [[]]
    j = 0

    for i in range(taille_grille):
        grille[j].append(pattern[i])

        if (i + 1) % dimensions[0] == 0 and (i + 1) != taille_grille:
            grille.append([])
            j += 1

    return grille


def est_gagnante(grille):
    "Renvoie vrai si la grille passée en paramètre est gagnante, faux sinon"

    tout_allume = True

    for i in grille:
        for j in i:
            if j == "5":
                tout_allume = False
    
    return tout_allume


def mise_a_jour_grille(grille):
    "Met à jour la grille (état des hélices) selon la position des ventilateurs"

    # remettre toutes les hélices en position éteinte
    for i_index, i in enumerate(grille):
        for j_index, j in enumerate(i):
            if j == "6":
                grille[i_index][j_index] = "5"

    # allumage des hélices dans le vent
    for i_index, i in enumerate(grille):
        for j_index, j in enumerate(i):

            # souffle en haut
            if j == "1":
                for k_index, k in reversed(list(enumerate(grille[:i_index]))):
                    if k[j_index] == "5":
                        grille[k_index][j_index] = "6"
                    elif k[j_index] == "B":
                        break

            # souffle à droite
            elif j == "2":
                for k_index, k in enumerate(grille[i_index][j_index:]):
                    if k == "5":
                        grille[i_index][j_index+k_index] = "6"
                    elif k == "B":
                        break

            # souffle en bas
            elif j == "3":
                for k_index, k in enumerate(grille[i_index:]):
                    if k[j_index] == "5":
                        grille[i_index+k_index][j_index] = "6"
                    elif k[j_index] == "B":
                        break

            # souffle à gauche
            elif j == "4":
                for k_index, k in reversed(list(enumerate(grille[i_index][:j_index]))):
                    if k == "5":
                        grille[i_index][k_index] = "6"
                    elif k == "B":
                        break

    return grille
