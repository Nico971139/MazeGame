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

	def waylist_contains(self):      # test
		for key, value in enumerate(self.way_list):
			return key, value


class MacGyver(Maze):
	"""Personnage principal"""
	def __init__(self):
		super().__init__()
		self.x = 1
		self.y = 0
		self.inventory = []

	def __str__(self):
		return "Mon personnage principal" # juste un petit test

	
	def top(self):
		try: 
			if self.grid[(self.x, self.y - 1)] == "0":  #vérifier que la destination n'est pas un mur
				self.y -= 1
				   									
			elif self.grid[(self.x, self.y - 1)] == "T" or "S" or "E": #vérifier s'il y a un objet ou non sur la case de destination
				self.inventory.append((self.x, self.y)) #ajouter l'objet ramassé dans le sac à dos de MacGyver
				self.grid[(self.x, self.y - 1)] = "0"  #"ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"

		except:  #vérifier que la destination n'est pas en dehors de la grille du labyrinthe
			pass
		
 		
 		
 		
 		#vérifier s'il y a le gardien ou non sur la case de destination

	def bot(self):
		try: 
			if self.grid[(self.x, self.y + 1)] == "0":  #vérifier que la destination n'est pas un mur
					self.y += 1
			elif self.grid[(self.x, self.y - 1)] == "T" or "S" or "E": #vérifier s'il y a un objet ou non sur la case de destination
				self.inventory.append((self.x, self.y))
				self.grid[(self.x, self.y - 1)] = "0"									   	
		except:       #vérifier que la destination n'est pas en dehors de la grille du labyrinthe
			pass		
			

	def left(self):
		try: 
			if self.grid[(self.x - 1, self.y)] == "0":  #vérifier que la destination n'est pas un mur
					self.x -= 1
			elif self.grid[(self.x, self.y - 1)] == "T" or "S" or "E": #vérifier s'il y a un objet ou non sur la case de destination
				self.inventory.append((self.x, self.y))
				self.grid[(self.x, self.y - 1)] = "0"									   	
		except:		#vérifier que la destination n'est pas en dehors de la grille du labyrinthe
			pass

	def right(self):
		try: 
			if self.grid[(self.x - 1, self.y)] == "0":  #vérifier que la destination n'est pas un mur
					self.x += 1
			elif self.grid[(self.x, self.y - 1)] == "T" or "S" or "E": #vérifier s'il y a un objet ou non sur la case de destination
				self.inventory.append((self.x, self.y))
				self.grid[(self.x, self.y - 1)] = "0"									   	
		except:				#vérifier que la destination n'est pas en dehors de la grille du labyrinthe
			pass


class Guardian(Maze):
	"""Le boss du labyrinthe"""
	def __init__(self):
		super().__init__()
		(self.x, self.y) = random.choice(self.way_list)






if __name__ == '__main__':
	"""Fonction principale"""
	maze = Maze()
	macGyver = MacGyver()
	gardien = Guardian()
	macGyver.bot()
	print(maze.grid)
	#print(macGyver.x)
	#print(macGyver.y)
	print(gardien.x)
	print(gardien.y)

