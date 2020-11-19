# coding: utf-8

class Maze:
    """Ma grille aura 15 carrés de longueur et 15 carrés de largeur"""
    def __init__(self):
        """le labyrinthe est une grille."""
        self.grid = {}

    def read_maze(self):
        with open("Maze.txt","r") as maze_file: #ouvre le fichier
            contents = maze_file.read() #lire le fichier Maze.txt
            contents = contents.split()
            grid = {}
            for key,value in enumerate(contents):
                grid[key] = value
            for key in range(15):
                print(value * 3)
        

            


class MacGyver:
    """ personnage MacGyver"""
    pass

class Guardian:
    """ le gardien """
    pass



def main():
    """test pour creer une liste de liste"""
    maze = Maze()
    print(maze.read_maze())
    
    
main() 





