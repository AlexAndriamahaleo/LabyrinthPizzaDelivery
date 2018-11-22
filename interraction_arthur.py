# classe perso
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
		#Direction par défaut
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

	def is_interact (self, piece):
		self.position = (self.x, self.y)
		return self.position == piece.position

	def is_interact (self, pizza):
		self.position = (self.x, self.y)
		return self.position == pizza.position


# classe piece
class Piece:
    #on initialise la piece avec une valeur en x et une en y
    def __init__(self, x, y):
        #position en x
        self.x = x
        #position en y
        self.y = y
        #on met la pièce sur le plateau
        self.estSurPlateau = True
     
    def position(self):
        #on vérifie si la pièce est sur le plateau
        #si c'est le cas on affiche sa position
        if self.estSurPlateau:
            print ("La pièce se trouve en ({},{})" , format(self.x, self.y))
        else:
            print ("Cette pièce n'est plus sur le plateau")
 
    def changePosition(self, newx, newy):
        """ On change la valeur des positions"""
        if self.estSurPlateau:
            self.x = newx
            self.y = newy
        else:
            print ("Cette pièce n'est plus sur le plateau")
 
    def enleve(self):
        self.estSurPlateau = False
        print ("La pièce est retirée du plateau")

    def _int_(self, x, y):
            self.x, self.y =x, y
            self.position = (self.x, self.y)


#Classe Pizza
class Pizza:
    def _int_(self, x, y):
        self.x=x
        self.y=y
        self.SurPlateau= True
    def position(self):
        if self.SurPlateau:
            print ("La pizza se trouve en (x,y)" ,format(self.x,self.y))
        else:
            print ("Cette pizza n'est plus sur le plateau")

    def changePosition (self, newx, newy):
        if self.SurPlateau:
            self.x=newx
            self.y=newy
        else:
            print ("Cette pizza n'est plus sur le plateau")

    def enleve(self):
        self.SurPlateau= False
        print ("La pizza est retirée du plateau")
   
    def _int_(self, x, y):
            self.x, self.y =x, y
            self.position = (self.x, self.y)
