""" Module qui permet d'ajouter l'animation d'une image en fonction d'une fenêtre, d'un nom de dossier 
qui contient les sprites.
Le module va créer l'animation
Pour utiliser le module indiquer :
import animation
from animation import *
Le module importe pour lui-même pygame,glob, sys
"""

import pygame, glob, sys
from pygame.locals import *
pygame.init()

def animation_image(plateau,nom_dossier):

# Données de base
    boucle = 1
#Récupération de la fenetre
    fenetre = plateau.fenetre

#Creation de l'animation
    class animation:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.ani = glob.glob(nom_dossier) #recupérer les frames dans une array \ a modif pour linux
            self.ani.sort() #met dans l'ordre la liste d'images
            self.ani_pos = 0 #position dans la liste
            self.ani_max = len(self.ani)-1 #nombres d'animations max (position max qu'on peut atteindre)
            self.ani_speed_init = 100 #vitesse de l'animation
            self.ani_speed = self.ani_speed_init #vitesse courante
            self.img = pygame.image.load(self.ani[0])
            self.update(0)

        def update(self,pos):
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
            #Ajout de la grille puis de l'animation
            fenetre.blit(plateau.grille,(0,0))
            fenetre.blit(self.img,(self.x,self.y))
            #Mise à jour de la fenêtre
            pygame.display.flip() 

    anim = animation()
    pos = 1

    while boucle==1:
        for event in pygame.event.get():
            if event.type ==QUIT:
                boucle=0
            #elif event.type == KEYDOWN and event.key== K_RIGHT:
                #pos = 1
            #elif event.type == KEYUP and event.key== K_RIGHT: 
                #pos = 0
            #elif event.type == KEYDOWN and event.key== K_LEFT:
                #pos = -1
            #elif event.type == KEYUP and event.key== K_LEFT: 
                #pos = 0 
        anim.update(pos) 
                    
                
                

