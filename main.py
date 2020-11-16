# coding: utf-8


"""Pour générer notre labyrinthe nous allons utilisé 
un algorithme de parcours en profondeur"""



class Square:
	"""Mon labyrinthe est un grille composé
		de plusieurs petits carrés entourés par des murs"""	

	
	def __init__(self): 
		"""on initialise notre classe carré.Avec nos 4 cotés."""
		self.top = True
		self.bottom = True
		self.left = True
		self.right = True
	

class Maze:
	"""Ma grille aura 15 carrés de longueur et 15 carrés de largeur"""
	def __init__(self):
		"""On creer la grille.Notre grille est en fait une liste
		qui contient 15 autres listes de carrés """
		self.a_list = []
		self.append(Square()) 
		


def main():
 """test pour creer une liste de liste"""
	liste_liste = []
	liste = []
	for x in range(15):
		liste.append(Square())

	for i in range(15):
		liste_liste.append(liste)
	print(liste_liste[4][5].top)
main() 





