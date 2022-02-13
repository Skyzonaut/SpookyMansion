#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      follioty
#
# Created:     27/04/2017
# Copyright:   (c) follioty 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame,sys
import time
from pygame.locals import*

#on initialise
pygame.init()
screen_taille = (1200, 800)
screen_surface = pygame.display.set_mode(screen_taille,0,32)
pygame.display.set_caption("Spooky Mansion")
background = pygame.image.load('map2.png')
screen_surface.blit(background,(0,0))


class Bob:
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bob.front.1.png").convert_alpha()
        self.pos = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def update():
        self.pos = (posx, posy)
        self.posx =+ change_x
        self.posy =+ change_y

    def mouvementhaut(self):
        self.change_y =+ 2
    def mouvementbas(self):
        self.change_y =- 2
    def mouvementgauche(self):
        self.change_x =- 2
    def mouvementdroit(self):
        self.change_x =+ 2


def main():

    bob = Bob()
    screen_surface.blit(bob.image, bob.pos)
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    mouvementbas()
                if event.key == K_UP:
                    mouvementhaut()
                if event.key == K_LEFT:
                    mouvementgauche()
                if event.key == K_RIGHT:
                    mouvementdroit()


while 1:
    main()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()





