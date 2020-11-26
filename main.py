# coding: utf-8
import random

class Maze:
	"""Une grille de 15 cellules par 15 cellule"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		self.maze_file = open("Maze.txt", "r")
		


	def read_maze(self):
		
		line = self.maze_file.readline() #lire le fichier ligne par ligne Maze.txt
		grid = {}
		lines = []
		while line != "":
			element = line.split()
			lines.append(element)
			print(element)
			line = self.maze_file.readline()

		for i, row in enumerate(lines):
			for x, y in enumerate(row):
				grid[i, x] = y
		
		return grid		
					      
		
			
	def waylist(self):
		"""Recuperer la liste de chemin"""
		text = self.maze_file.readline()
		way = {}
		waylist = {}
		matrix = []
		for i in text:
			liste = text.split()
			matrix.append(liste)
			text = self.maze_file.readline() 
			for i, row in enumerate(matrix):
				for x, y in enumerate(row):
					way[i, x] = y

		for key, value in way.items():
			if value == "0":
				waylist[key] = value
			else:
				pass

		return waylist		
				
		


		
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

class Items:
	""" les objets """
	def __init__(self):
		self.char = "Z"
	
	def random_position(self):
		return [random.choice(k, v) for k, v in Maze.waylist.items()] 


def main():
	"""Fonction principale"""
	maze = Maze()
	macGyver = MacGyver()
	item = Items()
	print(item.random_position)

	
	
main() 





