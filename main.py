# coding: utf-8
import random

class Maze:
	"""Une grille de 15 cellules par 15 cellule"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		self.grid = {}
		self.way_list = []
		self.read_maze()
		self.set_objects()
		

	def read_maze(self):
		x, y = 0, 0
		with open("Maze.txt", "r") as line:
			l = line.read()
			for element in l:
				if element == '\n':
					x, y = 0, y+1
				else :
					self.grid[(x, y)] = element
					if element == "0":
						self.way_list.append((x, y))
					x += 1

	def set_objects(self):
		objects = ["T", "S", "E"]
		random.shuffle(self.way_list)
		for key, value in enumerate(objects):
			self.grid[self.way_list[key]] = value


class MacGyver:
	"""Personnage principal"""
	def __init__(self):
		pass


if __name__ == '__main__':
	"""Fonction principale"""
	maze = Maze()
	print(maze.grid)


