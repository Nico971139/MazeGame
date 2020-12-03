# coding: utf-8
import random


class Maze:
	"""Une grille de 15 cellules par 15 cellule"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		self.maze_file = open("Maze.txt", "r")
		self.grid = {}
		self.way_list = {}



	def read_maze(self):
		
		line = self.maze_file.readline() #lire le fichier ligne par ligne Maze.txt
		
		lines = []
		while line != "":
			element = line.split()
			lines.append(element)
			#print(element)
			line = self.maze_file.readline()

		for i, row in enumerate(lines):
			for x, y in enumerate(row):
				self.grid[i, x] = y

	
	def waylist(self):
		"""Recuperer la liste de chemin"""

		for key,value in self.grid.items():
			if value == "0":
				self.way_list[key] = value
			else:
				pass
		
		"""for k in list(way):
			for n in range(3):	
				random.choice(list(way))"""
		
class MacGyver:
	""" personnage MacGyver"""
	def __init__(self):
		pass

	def movement(self):
		pass

	def takeItems(self):
		pass


class Guardian:
	""" le gardien """
	pass

class Items(Maze):
	""" les objets """
	def __init__(self ):
		super().__init__()
		self.characters = "Z"
		self.position = [random.choice(self.way_list.key()) for k in self.way_list]
			
	"""def put_items(self):
		for k in list(self.way_list):
			for n in range(3):
				print(random.choice(list(self.way_list)))"""
			
				

	

def main():
	"""Fonction principale"""
	maze = Maze()
	macGyver = MacGyver()
	maze.read_maze()
	maze.waylist()
	items = Items() #Initialiser les objets
	items.read_maze()
	items.waylist()
	#Positioner les objet sur les chemins
	print(items.way_list)
	
	



	
main() 





