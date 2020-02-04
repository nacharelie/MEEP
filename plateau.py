""" Module qui permet de créer un plateau de jeu en fonction d'une longeur,
d'une largeur, d'un nombre de cases et d'une image de fond. 
La largeur doit être au moins de 400
La fonction retourne un plateau avec comme attribut : une fenetre, un fond et une grille
Pour utiliser le module indiquer :
import plateau
from plateau import *
Le module importe pour lui-même pygame
"""
import pygame
from pygame.locals import *
pygame.init()


def genere_plateau(width, height, nbCases,image_fond):

#Creation du plateau
    class plateau:
        def __init__(self):
            self.fenetre = pygame.display.set_mode((width, height))
            self.fond = pygame.image.load(image_fond).convert()
            self.grille = pygame.display.get_surface().copy() #initialisation à vide

# Données de base
    boucle = 1
    NOIR = (0, 0, 0)

# Fenetre
    plateau1 = plateau()
    fenetre = plateau1.fenetre
    x = width - 200
    y = height
    fenetre.fill((254, 254, 254))
    fenetre.blit(plateau1.fond,(0,0))

# Lignes
    posX = 0
    posY = 0

# Lignes horizontales
    while posX <= x:
        pygame.draw.line(fenetre, NOIR, (posX, 0), (posX, y), 2)
        posX = posX + int(x/nbCases)
        pygame.display.flip()


# Lignes verticales
    while posY<=y:
        pygame.draw.line(fenetre,NOIR,(0,posY),(x,posY),2)
        posY = posY + int(y/nbCases) 
        pygame.display.flip()
    
    plateau1.grille = pygame.display.get_surface().copy()

    return plateau1