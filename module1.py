#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      follioty
#
# Created:     23/03/2017
# Copyright:   (c) follioty 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame,sys
import time
from pygame.locals import*

def intro():
    #on initialise
    pygame.init()
    pygame.font.init()
    screen_taille = (1200, 800)
    screen_surface = pygame.display.set_mode(screen_taille,0,32)
    pygame.display.set_caption("Spooky Mansion")

    #temps
    timer = pygame.time.Clock()
    temps = timer.tick()/1000 # en seconde

    white = (255, 255, 255)
    black = (0, 0, 0)
    marron = (81, 58, 28)

    #boucle des evenements
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #ajouter l'event


        background = pygame.image.load('SnesMansionFireplaceFrame1.png')
        screen_surface.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen_surface.fill(white)
        pygame.time.wait(80)



        background = pygame.image.load('SnesMansionFireplaceFrame2.png')
        screen_surface.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen_surface.fill(white)
        pygame.time.wait(80)



        background = pygame.image.load('SnesMansionFireplaceFrame3.png')
        screen_surface.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen_surface.fill(white)
        pygame.time.wait(80)

if __name__ == '__main__': intro()



