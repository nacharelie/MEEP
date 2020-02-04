import pygame, glob, sys
from pygame.locals import *
pygame.init()

#Données
boucle = 1
#Creation de la fenetre
fenetre = pygame.display.set_mode((1000,650))
x,y = pygame.display.get_surface().get_size()
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond,(0,0))
pygame.display.flip()

#Creation du personnage
class player:
    def __init__(self):
        self.x = 100
        self.y = 100
        self.ani = glob.glob("helices/p*.png") #recupérer les frames dans une array \ a modif pour linux
        self.ani.sort() #met dans l'ordre la liste d'images
        self.ani_pos = 0 #position dans la liste
        self.ani_max = len(self.ani)-1 #nombres d'animations max (position max qu'on peut atteindre)
        self.ani_speed_init = 200 #vitesse de l'animation
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
        fenetre.blit(fond,(0,0))
        fenetre.blit(self.img,(self.x,self.y))

player1 = player()
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
    player1.update(pos)    
    pygame.display.flip()  
                    
                
                

