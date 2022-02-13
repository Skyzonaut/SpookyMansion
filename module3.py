#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      follioty
#
# Created:     04/05/2017
# Copyright:   (c) follioty 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import pygame,sys
from pygame.locals import*
from pygame import (K_Z, K_S, K_Q, K_D)
pygame.init()

class Bob(pygame.sprite.Sprite):
    """classe du personnage"""



#initialisation
    def _init_(self):
        super()._init_()
        self.image= pygame.image.load('Bob.front.1.png').convert_alpha()
        self.rect= self.image.get_rect()


        self.change_x=0
        self.change_y=0

    def update(self):
        """mouvement du personnage"""
        #mouvement gauche et droite
        self.rect.x += self.change_x
        #mouvement haut et bas
        self.rect.y += self.change_y
        if self.rect.y >= 800 - self.rect.height and self.change_y>=0:
            self.change_y=0
            self.rect.y=800-self.rect.height
        if self.rect.y<=0 and self.change_y<=0:
            self.change_y=0
            self.rect.y=0
        if self.rect.x<=0 and self.change_x<=0:
            self.change_x=0
            self.rect.x=0
        if self.rect.x >= 1200-self.rect.width and self.change_x>=0:
            self.change_x=0
            self.rect.x=1200-self.rect.width
        #definition de l'image de bob
        if self.change_y <0:
            self.image.load('Bob.back.2.png').convert_alpha()
        if self.change_y>0:
            self.image.load('Bob.Front.1.png').convert_alpha()
        if self.change_y==0:
            self.image.load().convert_alpha()
        if self.change_x<0:
            self.image.load ('Bob.left.1.png').conver_alpha
        if self.change_x>0:
            self.image.load('Bob.right.1.png').convert_alpha
        if self.change_x==0:
            self.image.load('').convert_alpha
        screen.blit(self.image,(300,300))

        #deplacement personnage

    def mvthaut(self):
        self.change_y=-8
    def mvtbas(self):
        self.change_y=8
    def mvtdroite(self):
        self.change_x=8
    def mvtgauche(self):
        self.change_y=-8

class ennemi(pygame.sprite.Sprite):
    """Classe des ennemis"""



def main():
    """ programe principale"""
    pass
    pygame.init()

    screen=pygame.display.set_mode((1200,800)) #definition de la fenetre
    pygame.display.set_caption("Spooky mansion")#donne un titre a la fenetre

    if event.type == pygame.K_Z: #touche Z pour aller vers le haut
        bob.mvthaut()
    if event.type==pygame.K_S: #touche S pour aller vers le bas
        bob.mvtbas()
    if event.type==pygame.K_Q: #touche Q pour aller vers la gauche
        bob.mvtgauche()
    if event.type==pygame.K_D: #touche D pour aller vers la droite
        bob.mvtdroite()



while 1:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        active_sprite_liste=pygame.sprite.Group()


if __name__ == '__main__':
    main()
