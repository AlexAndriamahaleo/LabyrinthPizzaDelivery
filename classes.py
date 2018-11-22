import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
  
  def __init__(self, fichier):
          self.fichier = fichier
          self.structure = 0
  
  
  def generer(self):
          with open(self.fichier, "r") as fichier:
                  structure_niveau = []
                  for ligne in fichier:
                          ligne_niveau = []
                          for sprite in ligne:
                                  if sprite != '\n':
                                          ligne_niveau.append(sprite)
                          structure_niveau.append(ligne_niveau)
                  self.structure = structure_niveau
  
  
  def afficher(self, fenetre):
          mur = pygame.image.load(image_mur).convert()
          depart = pygame.image.load(image_depart).convert()
          arrivee = pygame.image.load(image_arrivee).convert_alpha()
          
          num_ligne = 0
          for ligne in self.structure:
                  num_case = 0
                  for sprite in ligne:
                          x = num_case * taille_sprite
                          y = num_ligne * taille_sprite
                          if sprite == 'm':		   #m = Maison
                                  fenetre.blit(mur, (x,y))
                          elif sprite == 'd':		   #d = Depart
                                  fenetre.blit(depart, (x,y))
                          elif sprite == 'a':		   
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'b':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'v':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'c':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'w':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'q':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'l':
                                  fenetre.blit(arrivee, (x,y))
                          elif sprite == 'f':
                                  fenetre.blit(arrivee, (x,y))
                          num_case += 1
                  num_ligne += 1
                  
                  
                  
                    
class Perso:
  def __init__(self, droite, gauche, haut, bas, niveau):
          #Sprites du personnage
          self.droite = pygame.image.load(droite).convert_alpha()
          self.gauche = pygame.image.load(gauche).convert_alpha()
          self.haut = pygame.image.load(haut).convert_alpha()
          self.bas = pygame.image.load(bas).convert_alpha()
          #Position du personnage en cases et en pixels
          self.case_x = 0
          self.case_y = 0
          self.x = 0
          self.y = 0
          #Direction par defaut
          self.direction = self.droite
          #Niveau dans lequel le personnage se trouve 
          self.niveau = niveau
  
  
  def deplacer(self, direction):
          if direction == 'droite':
                  if self.case_x < (nombre_sprite_cote - 1):
                          if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                                  self.case_x += 1
                                  self.x = self.case_x * taille_sprite
                  self.direction = self.droite
          
          if direction == 'gauche':
                  if self.case_x > 0:
                          if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                                  self.case_x -= 1
                                  self.x = self.case_x * taille_sprite
                  self.direction = self.gauche
          
          if direction == 'haut':
                  if self.case_y > 0:
                          if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                                  self.case_y -= 1
                                  self.y = self.case_y * taille_sprite
                  self.direction = self.haut
          
          if direction == 'bas':
                  if self.case_y < (nombre_sprite_cote - 1):
                          if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                                  self.case_y += 1
                                  self.y = self.case_y * taille_sprite
                  self.direction = self.bas
