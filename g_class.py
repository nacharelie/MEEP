""" Module qui conient les classes définit pour l'utilisation grpahique : 
    une classe pour l'animation
    une classe pour la fenetre 
Pour utiliser le module indiquer :
import g_class
from g_class import *
Le module importe pour lui-même pygame,glob, sys
"""

import pygame, glob, sys
from pygame.locals import *
pygame.init()

#Classe pour l'animation
class animation:
    def __init__(self,plateau,nom_dossier,x,y):
        self.x = x
        self.y = y
        self.ani = glob.glob(nom_dossier) #recupérer les frames dans une array \ a modif pour linux
        self.ani.sort() #met dans l'ordre la liste d'images
        self.ani_pos = 0 #position dans la liste
        self.ani_max = len(self.ani)-1 #nombres d'animations max (position max qu'on peut atteindre)
        self.ani_speed_init = 100 #vitesse de l'animation
        self.ani_speed = self.ani_speed_init #vitesse courante
        self.img = pygame.image.load(self.ani[0])
        self.update(0,plateau)

    def update(self,pos,plateau):
        if pos!=0:
            self.ani_speed = self.ani_speed-1
            #self.x = self.x+pos #besoin de quelque chose de statique
            if self.ani_speed ==0:
                self.img = pygame.image.load(self.ani[self.ani_pos]).convert_alpha()
                self.ani_speed = self.ani_speed_init
                if self.ani_pos == self.ani_max:
                    self.ani_pos = 0
                else:
                    self.ani_pos = self.ani_pos+1
        #Ajout de l'animation
        plateau.fenetre.blit(self.img,(self.x,self.y))

#Classe du plateau
class plateau:
    #Initialise le plateau
    def __init__(self,width, height, nbCases,image_fond):
        self.fenetre = pygame.display.set_mode((width, height))
        self.fond = pygame.image.load(image_fond).convert()
        self.nbCases = nbCases
        
    #Initialise la grille et retourne le fond (image+lignes)
    def grille(self):
    # Données de base
        NOIR = (0, 0, 0)
        posX = 0
        posY = 0

    # Fenetre
        x,y = pygame.display.get_surface().get_size()
        fenetre = self.fenetre
        x = x - 200
        fenetre.fill((254, 254, 254))
        fenetre.blit(self.fond,(0,0))

    # Lignes
        posX = 0
        posY = 0

    # Lignes horizontales
        while posX <= x:
            pygame.draw.line(fenetre, NOIR, (posX, 0), (posX, y), 2)
            posX = posX + int(x/self.nbCases)
            pygame.display.flip()


    # Lignes verticales
        while posY<=y:
            pygame.draw.line(fenetre,NOIR,(0,posY),(x,posY),2)
            posY = posY + int(y/self.nbCases) 
            pygame.display.flip()

        fondGrille = pygame.display.get_surface().copy()
        return fondGrille
