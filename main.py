# coding: utf-8
import random

class Maze:
	"""Une grille de 15 cellules par 15 cellule"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		self.grid = {}
		self.way_list = []
		self.macGyver = None
		self.guardian = None
		self.inventory = []
		self.read_maze()
		self.set_objects()
		

	def read_maze(self):
		"""On va lire le fichier maze.txt et 
		pour chaque element du fichier on lui
		attribut une abscisse et une ordonnée"""
		x, y = 0, 0
		with open("Maze.txt", "r") as line:
			l = line.read()
			# pour chaque element du fichier
			for element in l:
				# si on va à la ligne
				if element == '\n':
					x, y = 0, y+1
				else :
					self.grid[(x, y)] = element
					if element == "0":
						self.way_list.append((x, y))
					if element == "D":
						self.macGyver = x, y 
					if element == "F":
						self.guardian = x, y
					x += 1

	def set_objects(self):
		"""crée une liste d'objets qu'on 
		place aleatoirement sur le chemin"""
		objects = ["T", "S", "E"]
		random.shuffle(self.way_list)
		for key, value in enumerate(objects):
			self.grid[self.way_list[key]] = value

	########################
	###### DESTINATION #####
	########################             

	def check_move(self, a, b):
		"""vérifier que la destination n'est pas un mur"""
		"""vérifier que la destination n'est pas en dehors de la grille du labyrinthe"""
		return ((a, b) in self.grid and self.grid[a, b] != "#")

	def check_items(self, a, b):
		"""	vérifier s'il y a un objet ou non sur la case de destination
			"ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"
			ajouter l'objet ramassé dans le sac à dos de MacGyver"""
		if self.grid[a, b] == "T" or self.grid[a, b] == "S" or self.grid[a, b] ==  "E":
			self.inventory.append(self.grid[a, b])
			print(self.grid[a, b])
			self.grid[a, b] = "0"

	def check_pos_guardian(self, a, b):
		"""vérifier s'il y a le gardien
		ou non sur la case de destination"""
		if self.grid[a, b] == self.grid[self.guardian]:
			if len(self.inventory) == 3:
				print("You win")
			else:
				print("Repose en paix, fils du Gondor.")
		
	########################
	######    MOVES    #####
	########################
	def top(self):
		x = self.macGyver[0]
		y = self.macGyver[1] - 1
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)

	def bot(self):
		x = self.macGyver[0]
		y = self.macGyver[1] + 1
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)


	def left(self):
		x = self.macGyver[0] - 1
		y = self.macGyver[1] 
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)

	def right(self):
		x = self.macGyver[0] + 1 
		y = self.macGyver[1] 
		if self.check_move(x, y):
			self.macGyver = x, y
			self.check_items(x, y)
			self.check_pos_guardian(x, y)
	
class MacGyver():
	"""Personnage principal"""
	def __init__(self):
		self.x = x
		self.y = y
		self.inventory = []





if __name__ == '__main__':
	"""Fonction principale"""
	maze = Maze()
	maze.bot()
	maze.bot()
	maze.right()
	maze.right()
	#maze.check_way()
	print(maze.grid[maze.guardian])
	print(maze.macGyver)
	print(maze.inventory)
	
	
	
	

