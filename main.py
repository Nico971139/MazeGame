# coding: utf-8

class Maze:
    """Ma grille aura 15 carrés de longueur et 15 carrés de largeur"""
    def __init__(self):
        """le labyrinthe est une grille."""
        self.grid = {}

    def read_maze(self):
        with open("Maze.txt","r") as maze_file: #ouvre le fichier
            line = maze_file.readline() #lire le fichier ligne par ligne Maze.txt
            grid = {}
            lines = []
            for element in line:
                element = line.split()
                lines.append(element)
                print(element)
                line = maze_file.readline() #ligne suivante
            for i, row in enumerate(lines):
                for x, y in enumerate(row):
                    grid[i, x] = y
            print(grid)
            
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





