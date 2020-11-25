# coding: utf-8

class Maze:
	"""Ma grille aura 15 carrés de longueur et 15 carrés de largeur"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		pass

	def read_maze(self):
		with open("Maze.txt","r") as maze_file: #ouvre le fichier
			line = maze_file.readline() #lire le fichier ligne par ligne Maze.txt
			grid = {}
			lines = []
			while line != "":
				element = line.split()
				lines.append(element)
				print(element)
				line = maze_file.readline()    
			for i, row in enumerate(lines):
				for x, y in enumerate(row):
					grid[i, x] = y
			for key, value in grid.items():
					#print(key,value)
					pass      
			# grid([x, y]) = "chemin"
			# grid([x, y]) = "McGyver"
			# grid([x, y]) = "Gardien"
			
			
	def waylist(self):
		with open("Maze.txt","r") as maze_file:
			way = maze_file.readline()
			while way != "":
				true_way = way.replace("#", " ")
				print(true_way)
				way = maze_file.readline()
				
			
class MacGyver:
	""" personnage MacGyver"""
	def __init__(self):
		self.health = 10
		self.max_health = 10
		self.attack = 0
		self.speed = 1

	def movement(self):
		pass

class Guardian:
	""" le gardien """
	pass

class Items:
	""" les objets """
	pass

def main():
	"""Fonction principale"""
	maze = Maze()
	print(maze.read_maze())

	
	
main() 





