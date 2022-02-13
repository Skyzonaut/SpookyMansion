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

def main():
    #on initialise
    pygame.init()
    pygame.font.init()
    screen_taille = (1200, 800)
    screen_surface = pygame.display.set_mode(screen_taille,0,32)
    pygame.display.set_caption("Spooky Mansion")
    player = pygame.image.load('Bob.front.1.png').convert_alpha()
    background = pygame.image.load('SnesMansionFireplaceFrame1.png')
    screen_surface.blit(background,(0,0))
    position = player.get_rect()
    for i in range (100):
        position.x += 5
        screen_surface.blit(player, position)
        pygame.display.update()

pygame.init()
while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        main()

