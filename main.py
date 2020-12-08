# coding: utf-8
import random

class Maze:
	"""Une grille de 15 cellules par 15 cellule"""
	def __init__(self):
		"""le labyrinthe est une grille."""
		self.grid = {}
		self.way_list = []
		self.objects = {}
		self.read_maze()
		self.set_objects()
		self.objects_list()

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

	def objects_list(self):
		for key, value in self.grid.items():
			self.grid[key] = value
			if value == "T":
				self.objects[key] = value
			if value == "S":
				self.objects[key] = value
			if value == "E":
				self.objects[key] = value

class MacGyver(Maze):
	"""Personnage principal"""
	def __init__(self, x, y):
		super().__init__()
		self.x = x
		self.y = y
		self.position = (self.x, self.y)
		self.new_position = ()
		self.inventory = []
		self.take_item()


	def __str__(self):
		return "Mon personnage principal" # juste un petit test


	def check_way(self):
		
		if self.new_position in self.way_list:
			return self.new_position
		else:
			print("Vous ne passerez pas")
			pass
			

	def take_item(self):
		"""S'il y  a un objet sur le chemin on 
		le ramasse et on le met dans le sac"""
		if self.new_position in self.objects:						#vérifier s'il y a un objet ou non sur la case de destination
		 	for key, value in self.objects.items():			            #ajouter l'objet ramassé dans le sac à dos de MacGyver
		 		self.new_position[key] = value
		 		self.inventory.append(value)		            #"ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"



	def top(self):
		self.y = self.y - 1
		self.new_position = self.x, self.y
		return self.new_position
		
 		
	def bot(self):
		self.y = self.y + 1
		self.new_position = self.x, self.y
		return self.new_position
		
		

	def left(self):
		self.x = self.x - 1
		self.new_position = self.x, self.y
		return self.new_position
		

	def right(self):
		self.x = self.x + 1
		self.new_position = self.x, self.y
		return self.new_position 


class Guardian(Maze):
	"""Le boss du labyrinthe"""
	def __init__(self):
		super().__init__()
		(self.x, self.y) = random.choice(self.way_list)






if __name__ == '__main__':
	"""Fonction principale"""
	maze = Maze()
	macGyver = MacGyver(1, 0)
	gardien = Guardian()
	#print(maze.way_list)
	macGyver.bot()
	macGyver.bot()
	macGyver.right()
	print(maze.grid)
	print(macGyver.new_position)
	print(maze.objects)
	print(macGyver.inventory)
	"""for k, v in maze.objects.items():
		print(k, v)"""
	

