import pygame
import time
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenetre Pygame
fenetre = pygame.display.set_mode((750, 750))
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
pygame.mixer.music.load("son/technogenerator.wav")


#Boucle principale
continuer = 1
continuer_aide = 1
x = 0
y = 0
while continuer:
        
        
        while continuer_aide :
                aide = pygame.image.load(image_aide).convert()
                fenetre.blit(aide, (0,0))
                pygame.display.flip()
                pygame.time.wait(5000)
                continuer_aide = 0



        accueil = pygame.image.load(image_accueil).convert()
        fenetre.blit(accueil, (0,0))
        pygame.display.flip()
        pygame.mixer.music.load("son/technogenerator.wav")
        pygame.mixer.music.play()

        continuer_jeu = 1
        continuer_accueil = 1
      

        
        
        # Boucle de la page d'accueil du jeu
        while continuer_accueil:                
                pygame.time.Clock().tick(30)
                

                for event in pygame.event.get():

                        
                        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                                pygame.mixer.music.stop()                                
                                pygame.quit()

                                               
#lvl 1
                        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and  565 > event.pos[1] > 510 and 705 > event.pos[0] > 499 :
                                pygame.mixer.music.stop()
                                continuer_accueil = 0
                                choix = 'n1'
#lvl 2
                        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and  639 > event.pos[1] > 579 and 705 > event.pos[0] > 499:
                                pygame.mixer.music.stop()
                                continuer_accueil = 0
                                choix = 'n11'
#lvl 3
                        elif event.type == MOUSEBUTTONDOWN and event.button == 1 and  703 > event.pos[1] > 648 and 705 > event.pos[0] > 499:
                                pygame.mixer.music.stop()
                                continuer_accueil = 0
                                choix = 'n111'

                        
        if choix !=0:
                fond = pygame.image.load(image_fond).convert()
                niveau = Niveau(choix)
                niveau.generer()
                niveau.afficher(fenetre)
                nick = Perso("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)
                pygame.mixer.music.load("son/startpress.wav")
                pygame.mixer.music.play()

				
	#Boucle du jeu
        while continuer_jeu:
                

                pygame.time.Clock().tick(30)
                
                for event in pygame.event.get():

                        if event.type == QUIT:
                                continuer_jeu = 0
                                continuer_aide = 0
                                continuer = 0

                        elif event.type == KEYDOWN:
				
                                if event.key == K_ESCAPE:
                                        pygame.mixer.music.stop()
                                        continuer_jeu = 0
                                        


                                elif event.key == K_RIGHT:
                                        nick.deplacer('droite')
                                elif event.key == K_LEFT:
                                        nick.deplacer('gauche')
                                elif event.key == K_UP:
                                        nick.deplacer('haut')
                                elif event.key == K_DOWN:
                                        nick.deplacer('bas')

                #Affichages aux nouvelles positions
                fenetre.blit(fond, (0,0))
                niveau.afficher(fenetre)
                fenetre.blit(nick.direction, (nick.x, nick.y)) 
                pygame.display.flip()


                #Niveau suivant
                if niveau.structure[nick.case_y][nick.case_x] == 'a':
                        continuer_jeu = 1
                        choix = 'n2'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y)) 
                        pygame.display.flip()
                        nick = Perso("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)

                elif niveau.structure[nick.case_y][nick.case_x] == 'b':
                        continuer_jeu = 1
                        choix = 'n3'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y))
                        pygame.display.flip()
                        nick = Perso ("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)



                elif niveau.structure[nick.case_y][nick.case_x] == 'w':
                        continuer_jeu = 1
                        choix = 'n22'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y))
                        pygame.display.flip()
                        nick = Perso ("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)

                elif niveau.structure[nick.case_y][nick.case_x] == 'q':
                        continuer_jeu = 1
                        choix = 'n33'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y))
                        pygame.display.flip()
                        nick = Perso ("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)

                elif niveau.structure[nick.case_y][nick.case_x] == 'l':
                        continuer_jeu = 1
                        choix = 'n222'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y))
                        pygame.display.flip()
                        nick = Perso ("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)

                elif niveau.structure[nick.case_y][nick.case_x] == 'f':
                        continuer_jeu = 1
                        choix = 'n333'
                        niveau = Niveau(choix)
                        niveau.generer()
                        niveau.afficher(fenetre)
                        fenetre.blit(fond, (0,0))
                        niveau.afficher(fenetre)
                        fenetre.blit(nick.direction, (nick.x, nick.y))
                        pygame.display.flip()
                        nick = Perso ("images/nickd.jpg","images/nickg.jpg","images/nickback.jpg","images/nickface.jpg", niveau)


                
                elif niveau.structure[nick.case_y][nick.case_x] == 'v':
                        pygame.mixer.music.stop()
                        continuer_jeu = 0
                        
                        		
			
			
                        





			
