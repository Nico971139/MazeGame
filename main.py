# coding: utf-8

class Maze:
    """Ma grille aura 15 carrés de longueur et 15 carrés de largeur"""
    def __init__(self):
        """le labyrinthe est une grille."""
        self.grid = {}

    def read_maze(self):
        with open("Maze.txt","r") as maze_file: #ouvre le fichier
            line = maze_file.readline() #lire le fichier ligne par ligne Maze.txt
            lines = line.split()
            grid = {}
            print(lines)
            """while line != "":
                print(lines)
                line = maze_file.readline()"""
            
            
            # grid([x, y]) = "chemin"
            # grid([x, y]) = "McGyver"
            # grid([x, y]) = "Gardien"
            
            
           
            
            
            

class MacGyver:
    """ personnage MacGyver"""
    pass
class Guardian:
    """ le gardien """
    pass



def main():
    """Fonction principale"""
    maze = Maze()
    print(maze.read_maze())
    
    
main() 





