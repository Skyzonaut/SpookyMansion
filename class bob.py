import pygame,sys
import time
from pygame.locals import*


#on initialise
pygame.init()
screen_taille = (1200, 800)
screen_surface = pygame.display.set_mode(screen_taille,0,32)
pygame.display.set_caption("Spooky Mansion")

#temps
timer = pygame.time.Clock()
temps = timer.tick()/1000 # en seconde

white = (255, 255, 255)
black = (0, 0, 0)

class Bob(pygame.sprite.Sprite):    #Sprite de bob

    #initialisation
    def _init_(self, change_x, change_y):
        super()._init_()
        self.image = pygame.image.load('Bob.front.1.png').convert_alpha()
        self.rect = self.image.get_rect()
        screen.blit(self, (rect_x,rect_y))

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
        if self.change_y<=0:
            self.image.load('Bob.back.2.png').convert_alpha()
        if self.change_y>=0:
            self.image.load('Bob.Front.1.png').convert_alpha()
        if self.change_x<=0:
            self.image.load ('Bob.left.1.png').conver_alpha
        if self.change_x>=0:
            self.image.load('Bob.right.1.png').convert_alpha

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

bob = Bob(600, 400)


#boucle des evenements
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background = pygame.image.load('map2.png')
    screen_surface.blit(background,(0,0))
