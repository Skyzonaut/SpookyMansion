
#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      yanis
#
# Created:     02/03/2017
# Copyright:   (c) eleve 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame,sys, random,time
from pygame.locals import*
from random import*

pygame.init()
screen_width=1200
screen_height=800

class Bob(pygame.sprite.Sprite):
    """classe du personnage"""

#initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('Bob.front.1.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=450
        self.rect.y=450
        self.change_x=0
        self.change_y=0

    def update(self):
        """mouvement du personnage"""
        #mouvement gauche et droite
        self.rect.x += self.change_x
        #mouvement haut et bas
        self.rect.y += self.change_y
        if self.rect.y >= 720 - self.rect.height and self.change_y>=0:
            self.change_y=0
            self.rect.y=720-self.rect.height
        if self.rect.y<=80 and self.change_y<=0:
            self.change_y=0
            self.rect.y=80
        if self.rect.x<=80 and self.change_x<=0:
            self.change_x=0
            self.rect.x=80
        if self.rect.x >= 1120-self.rect.width and self.change_x>=0:
            self.change_x=0
            self.rect.x=1120-self.rect.width
        #definition de l'image de bob
        if self.change_y <0:
            self.image=pygame.image.load('Bob.back.2.png').convert_alpha()
        if self.change_y>0:
            self.image=pygame.image.load('Bob.Front.1.png').convert_alpha()
        if self.change_y==0:
            self.image=pygame.image.load('Bob.Front.1.png').convert_alpha()
        if self.change_x<0:
            self.image=pygame.image.load ('Bob.left.1.png').convert_alpha()
        if self.change_x>0:
            self.image=pygame.image.load('Bob.right.1.png').convert_alpha()

        #collision avec le decors
        if 235 <= self.rect.x <= 391:
            self.change_x == 0

        #deplacement personnage

    def mvthaut(self):
        self.change_y=-3
    def mvtbas(self):
        self.change_y=3
    def mvtdroite(self):
        self.change_x=3
    def mvtgauche(self):
        self.change_x=-3
    def nomvt(self):
        self.change_y=0
        self.change_x=0


class fantomes(pygame.sprite.Sprite):      # Creation classe Voiture Bleu

    # initialisation
    def __init__(self,vitesse):
        super().__init__()
        #chargement de l'image
        self.image = pygame.image.load('ghost.front1.png').convert_alpha()
        # Capture du rectangle permettant de gerer la voiture
        self.rect = self.image.get_rect()
        self.change_x=vitesse


    def update(self):
        self.rect.x += self.change_x
        if self.rect.x>1000:
            self.change_x = -self.change_x
        if self.rect.x<200:
            self.change_x = -self.change_x

        if self.change_x<0:
            self.image=pygame.image.load ('ghost.left1.png').convert_alpha()
        if self.change_x>0:
            self.image=pygame.image.load('ghost.right1.png').convert_alpha()


class fantomesn1(pygame.sprite.Sprite):      # Creation classe Voiture Bleu

    # initialisation
    def __init__(self):
        super().__init__()
        #chargement de l'image
        self.image = pygame.image.load('ghost.front1.png').convert_alpha()
        # Capture du rectangle permettant de gerer la voiture
        self.rect = self.image.get_rect()
        self.change_x=2
        self.change_y=0

    def update(self):
        self.rect.x += self.change_x
        if self.rect.x == 1040:
            self.change_x= -2
        if self.rect.x == 100:
            self.change_x= 2

        if self.change_x<0:
            self.image=pygame.image.load ('ghost.left1.png').convert_alpha()
        if self.change_x>0:
            self.image=pygame.image.load('ghost.right1.png').convert_alpha()

class fantomesn2(pygame.sprite.Sprite):      # Creation classe Voiture Bleu

    # initialisation
    def __init__(self):
        super().__init__()
        #chargement de l'image
        self.image = pygame.image.load('ghost.front1.png').convert_alpha()
        # Capture du rectangle permettant de gerer la voiture
        self.rect = self.image.get_rect()
        self.change_x=1
        self.change_y=1

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x == 1030:
            self.change_x= -1
        if self.rect.x == 100:
            self.change_x= 1
        if self.rect.y == 650:
            self.change_y = -1
        if self.rect.y == 145:
            self.change_y = 1
        if self.rect.y == 650:
            self.change_y = -1

        if self.change_y <0:
            self.image=pygame.image.load('ghost.back1.png').convert_alpha()
        if self.change_y>0:
            self.image=pygame.image.load('ghost.front1.png').convert_alpha()
        if self.change_y==0:
            self.image=pygame.image.load('ghost.front1.png').convert_alpha()
        if self.change_x<0:
            self.image=pygame.image.load ('ghost.left1.png').convert_alpha()
        if self.change_x>0:
            self.image=pygame.image.load('ghost.right1.png').convert_alpha()


class grandboss(pygame.sprite.Sprite):      # Creation classe Voiture Bleu

    # initialisation
    def __init__(self):
        super().__init__()
        #chargement de l'image
        self.image=pygame.image.load ('boss.png').convert_alpha()
        # Capture du rectangle permettant de gerer la voiture
        self.rect = self.image.get_rect()
        self.rect.x=550
        self.rect.y=150
        self.change_x=0
        self.change_y=0


    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        if self.rect.x==1120:
            self.change_x=-self.change_x
        if self.rect.x==80:
            self.change_x=-self.change_x
        if self.rect.x == 1200:
            self.kill()
        if self.rect.x == 0:
            self.kill()
        if self.rect.y == 0:
            self.kill()
        if self.rect.y == 800:
            self.kill()




class murs1(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('murscollision.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=236
        self.rect.y=190

class murs2(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('murscollision.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=814
        self.rect.y=190

class murs3(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('murscollision2.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=233
        self.rect.y=528

class clefs(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('keys.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=575
        self.rect.y=650

class projectile(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('laser1.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.change_x=0
        self.change_y=0

    def update(self):
        self.rect.x+=self.change_x
        self.rect.y+=self.change_y
        if self.rect.x == 1200:
            self.kill
        if self.rect.x == 0:
            self.kill
        if self.rect.y == 0:
            self.kill
        if self.rect.y == 800:
            self.kill

##class projectile2(pygame.sprite.Sprite):
##    #initialisation
##    def __init__(self):
##        super().__init__()
##        self.image= pygame.image.load('laser2.png').convert_alpha()
##        self.rect= self.image.get_rect()
##        self.change_y=0
##        self.change_x=0

    def update(self):
        self.rect.x+=self.change_x
        self.rect.y+=self.change_y

class coffres(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('chesto1.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=60
        self.rect.y=70


    def update(self):
        if collisioncoffre==1:
            self.image= pygame.image.load('chest1.png').convert_alpha()

class coffres2(pygame.sprite.Sprite):
    #initialisation
    def __init__(self):
        super().__init__()
        self.image= pygame.image.load('chesto2.png').convert_alpha()
        self.rect= self.image.get_rect()
        self.rect.x=1200-120
        self.rect.y=70
        global collisioncoffre
        collisioncoffre=0
    def update(self):
        if collisioncoffre==1:
            self.image= pygame.image.load('chest2.png').convert_alpha()

def intro():
    #on initialise
    pygame.init()
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")


    #temps
    timer = pygame.time.Clock()
    temps = timer.tick()/1000 # en seconde

    white = (255, 255, 255)
    black = (0, 0, 0)
    marron = (81, 58, 28)

    #ajouter l'event
    continuer = True
    while continuer:
        background = pygame.image.load('SnesMansionFireplaceFrame1.png')
        screen.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen.fill(white)
        pygame.time.wait(80)

        background = pygame.image.load('SnesMansionFireplaceFrame2.png')
        screen.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen.fill(white)
        pygame.time.wait(80)

        background = pygame.image.load('SnesMansionFireplaceFrame3.png')
        screen.blit(background,(0,0))
        pygame.display.update()
        pygame.time.wait(80)
        screen.fill(white)
        pygame.time.wait(80)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                continuer = 0
    pygame.quit()

def transition1():
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")
    imagego=pygame.image.load('transition1.png').convert_alpha()
    screen.blit(imagego,(0, 0))
    pygame.display.update()

    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                continuer = 0
    pygame.quit()
    main2()

def gameover1():
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")
    imagego=pygame.image.load('gameover1.png').convert_alpha()
    screen.blit(imagego,(0, 0))
    pygame.display.update()
    pygame.time.delay(10000)
    main1()

def gameover2():
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")
    imagego=pygame.image.load('gameover2.png').convert_alpha()
    screen.blit(imagego, (0, 0))
    pygame.display.update()
    pygame.time.delay(5000)
    main2()






""" programe principale"""


def main1():


    pygame.init()
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")#donne un titre a la fenetre
    fond=pygame.image.load('map2.png').convert_alpha()
    son=pygame.mixer.Sound("sonN1.wav")
    son.play(loops=-1, maxtime=0, fade_ms=0)
##    son=pygame.mixer.Sound("son ambiance niveaux 1.wav.wav")
    ##son.play(loops=-1, maxtime=0, fade_ms=0)

    #creation des sprites
    active_sprite_list=pygame.sprite.Group()
    fantome_sprite_list=pygame.sprite.Group()
    murs_sprite_list=pygame.sprite.Group()
    murs2_sprite_list=pygame.sprite.Group()
    murs3_sprite_list=pygame.sprite.Group()
    clef_sprite_list=pygame.sprite.Group()
    clef2_sprite_list=pygame.sprite.Group()
    clef3_sprite_list=pygame.sprite.Group()
    lasers_sprite_list=pygame.sprite.Group()
    chests_sprite_list=pygame.sprite.Group()
    chests2_sprite_list=pygame.sprite.Group()

    bob=Bob()
    active_sprite_list.add(bob)
    fantome=fantomes(1)
    fantome.rect.x = 300
    fantome.rect.y = 630

    fantome_sprite_list.add(fantome)
    active_sprite_list.add(fantome)

    mur1=murs1()
    murs_sprite_list.add(mur1)
    active_sprite_list.add(mur1)

    mur2=murs2()
    murs2_sprite_list.add(mur2)
    active_sprite_list.add(mur2)

    mur3=murs3()
    murs3_sprite_list.add(mur3)
    active_sprite_list.add(mur3)

    clef=clefs()
    cle=0
    clef_sprite_list.add(clef)
    active_sprite_list.add(clef)

    chest=coffres()
    chests_sprite_list.add(chest)
    active_sprite_list.add(chest)

    chest2=coffres2()
    chests2_sprite_list.add(chest2)
    active_sprite_list.add(chest2)

    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:   #touche Z pour aller vers le haut
                    bob.mvthaut()
                if event.key==pygame.K_s: #touche S pour aller vers le bas
                    bob.mvtbas()
                if event.key==pygame.K_a: #touche Q pour aller vers la gauche
                    bob.mvtgauche()
                if event.key==pygame.K_d: #touche D pour aller vers la droite
                    bob.mvtdroite()
                if event.key==pygame.K_LEFT:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_x=-5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_RIGHT:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_x=5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_DOWN:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_y=5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_UP:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_y=-5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y

            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    bob.nomvt()
                if event.key==pygame.K_s:
                    bob.nomvt()
                if event.key==pygame.K_a:
                    bob.nomvt()
                if event.key==pygame.K_d:
                    bob.nomvt()


        fantomes_hit_list=pygame.sprite.spritecollide(bob, fantome_sprite_list, False)
        for collision in fantomes_hit_list:
            son.stop()
            gameover1()

        murs_hit_list=pygame.sprite.spritecollide(bob, murs_sprite_list, False)
        for collision in murs_hit_list:
            bob.nomvt()
            if bob.rect.x>mur1.rect.x and bob.rect.y>mur1.rect.y:
                bob.rect.x += 5
            if bob.rect.x<mur1.rect.x and bob.rect.y>mur1.rect.y:
                bob.rect.x -= 5
            if mur1.rect.y<bob.rect.y :
                bob.rect.y+=5
            if mur1.rect.y>bob.rect.y :
                bob.rect.y-=5

        murs2_hit_list=pygame.sprite.spritecollide(bob, murs2_sprite_list, False)
        for collision in murs2_hit_list:
            bob.nomvt()
            if bob.rect.x>mur2.rect.x and bob.rect.y>mur2.rect.y:
                bob.rect.x += 5
            if bob.rect.x<mur2.rect.x and bob.rect.y>mur2.rect.y:
                bob.rect.x -= 5
            if mur2.rect.y<bob.rect.y :
                bob.rect.y+=5
            if mur2.rect.y>bob.rect.y :
                bob.rect.y-=5

        murs3_hit_list=pygame.sprite.spritecollide(bob, murs3_sprite_list, False)
        for collision in murs3_hit_list:
            bob.nomvt()
            if bob.rect.x>mur3.rect.x and bob.rect.y>mur3.rect.y:
                bob.rect.x += 5
            if bob.rect.x<mur3.rect.x and bob.rect.y>mur3.rect.y:
                bob.rect.x -= 5
            if mur3.rect.y<bob.rect.y :
                bob.rect.y+=5
            if mur3.rect.y>bob.rect.y :
                bob.rect.y-=5

        clef_hit_list=pygame.sprite.spritecollide(bob, clef_sprite_list, False)
        for collision in clef_hit_list:
            clef.kill()
            cle+=1

        laser_hit_list=pygame.sprite.groupcollide(lasers_sprite_list, fantome_sprite_list, True, True)
        for collision in laser_hit_list:
            laser.kill()
        lasermur_hit_list=pygame.sprite.groupcollide(lasers_sprite_list, murs_sprite_list, True, False)
        for collision in laser_hit_list:
            laser.kill()
        lasermur2_hit_list=pygame.sprite.groupcollide(lasers_sprite_list, murs2_sprite_list, True, False)
        for collision in laser_hit_list:
            laser.kill()
        lasermur3_hit_list=pygame.sprite.groupcollide(lasers_sprite_list, murs3_sprite_list, True, False)
        for collision in laser_hit_list:
            laser.kill()

        conu = 1
        chest_hit_list=pygame.sprite.groupcollide(chests_sprite_list, lasers_sprite_list, False, True)
        for collision in chest_hit_list:
            chest.image=pygame.image.load('chest1.png').convert_alpha()
            for conu in range (1):
                clef2=clefs()
                clef2_sprite_list.add(clef2)
                active_sprite_list.add(clef2)
                clef2.rect.x=140
                clef2.rect.y=125
                chests_sprite_list.remove(chest)
                conu += 1
        clef2_hit_list=pygame.sprite.spritecollide(bob, clef2_sprite_list, False)
        for collision in clef2_hit_list:
            clef2.kill()
            cle+=1
            conu = 0

        coni = 1
        chest2_hit_list=pygame.sprite.groupcollide(chests2_sprite_list, lasers_sprite_list, False, True)
        for collision in chest2_hit_list:
            chest2.image=pygame.image.load('chest2.png').convert_alpha()
            for coni in range (1):
                clef3=clefs()
                clef3_sprite_list.add(clef3)
                active_sprite_list.add(clef3)
                clef3.rect.x=1200-170
                clef3.rect.y=125
                chests2_sprite_list.remove(chest2)
                conu +=1
        clef3_hit_list=pygame.sprite.spritecollide(bob, clef3_sprite_list, False)
        for collision in clef3_hit_list:
            clef3.kill()
            cle+=1
            coni = 0






        # mise a jour du personnage
        active_sprite_list.update()

        #   affichage
        screen.blit(fond,(0,0))

        active_sprite_list.draw(screen)

        pygame.display.flip()


        if 480<bob.rect.x<720 and bob.rect.y==80 and cle == 0:
                continuer = 0
    pygame.quit()





""" programe secondaire"""

def main2():

##    pass
    pygame.init()
    size=[screen_width,screen_height]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Spooky mansion")#donne un titre a la fenetre
    fond=pygame.image.load('map4.png').convert_alpha()
    son=pygame.mixer.Sound("sonN1.wav")
    son.play(loops=-1, maxtime=0, fade_ms=0)
    tension = 0


    #creation des sprites
    active_sprite_list=pygame.sprite.Group()
    fantome_sprite_list=pygame.sprite.Group()
    lasers_sprite_list=pygame.sprite.Group()
    boss_sprite_list=pygame.sprite.Group()
    lasers2_sprite_list=pygame.sprite.Group()

    bob=Bob()
    active_sprite_list.add(bob)


    boss=grandboss()
    boss_sprite_list.add(boss)
    active_sprite_list.add(boss)

##    laser2=projectile2()
##    lasers2_sprite_list.add(laser2)
##    active_sprite_list.add(laser2)

    continuer=1
    while continuer:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:   #touche Z pour aller vers le haut
                    bob.mvthaut()
                if event.key==pygame.K_s: #touche S pour aller vers le bas
                    bob.mvtbas()
                if event.key==pygame.K_a: #touche Q pour aller vers la gauche
                    bob.mvtgauche()
                if event.key==pygame.K_d: #touche D pour aller vers la droite
                    bob.mvtdroite()
                if event.key==pygame.K_LEFT:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_x=-5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_RIGHT:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_x=5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_DOWN:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_y=5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
                if event.key==pygame.K_UP:
                    laser=projectile()
                    lasers_sprite_list.add(laser)
                    active_sprite_list.add(laser)
                    laser.change_y=-5
                    laser.rect.x=bob.rect.x
                    laser.rect.y=bob.rect.y
            if event.type == pygame.KEYUP:
                if event.key==pygame.K_w:
                    bob.nomvt()
                if event.key==pygame.K_s:
                    bob.nomvt()
                if event.key==pygame.K_a:
                    bob.nomvt()
                if event.key==pygame.K_d:
                    bob.nomvt()



        tension = 550
        if tension < 500:

            """1"""
            if randint(1,500)==2:
                fantome1=fantomesn1()
                fantome1.rect.x = 1030
                fantome1.rect.y = 460
                fantome_sprite_list.add(fantome1)
                active_sprite_list.add(fantome1)
                tension +=5


            """2"""
            if randint(1,500)==2:
                fantome2=fantomesn1()
                fantome2.rect.x = 120
                fantome2.rect.y = 300
                fantome_sprite_list.add(fantome2)
                active_sprite_list.add(fantome2)
                tension +=5


            """3"""
            if randint(1,500)==2:
                fantome3=fantomesn2()
                fantome3.rect.x = 120
                fantome3.rect.y = 647
                fantome_sprite_list.add(fantome3)
                active_sprite_list.add(fantome3)


            """4"""
            if randint(1,500)==2:
                fantome4=fantomesn2()
                fantome4.rect.x = 1020
                fantome4.rect.y = 647
                fantome_sprite_list.add(fantome4)
                active_sprite_list.add(fantome4)


        if tension > 500:
            if bob.change_x !=0 :
                boss.change_x=-bob.change_x
                boss.change_y=-bob.change_y
            if bob.change_x ==0:
                boss.change_x = 0
            if bob.change_y == 0:
                boss.change_y =0


        fantomes_hit_list=pygame.sprite.spritecollide(bob, fantome_sprite_list, False)
        for collision in fantomes_hit_list:
            son.stop()
            gameover2()

        laser_hit_list=pygame.sprite.groupcollide(lasers_sprite_list, fantome_sprite_list, True, True)
        for collision in laser_hit_list:
            laser.kill()

        vie = 15
        boss_hit_list=pygame.sprite.spritecollide(laser,boss_sprite_list, False)
        if boss.change_x != 0:
            for collision in boss_hit_list:
                if boss.change_x != 0:
                    laser.kill()
                    vie -= 1
                    boss.image=pygame.image.load('bossAHPUTAINJAIMAL.png').convert_alpha()
                    pygame.time.delay(5)
                boss.image=pygame.image.load ('boss.png').convert_alpha()
        if vie == 0:
            boss.kill()


        clock = pygame.time.Clock()

        # mise a jour du personnage
        active_sprite_list.update()

        #   affichage
        screen.blit(fond,(0,0))

        active_sprite_list.draw(screen)

        pygame.display.flip()

        clock = pygame.time.Clock()
        clock.tick(1000)








intro()
main1()
transition1()
main2()





