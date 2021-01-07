# coding: utf-8
import random
import pygame
from settings import ( BLACK, WHITE, WIN, LOSE, 
SIZE, WIDTH, HEIGHT, CENTER )

class Maze(pygame.sprite.Sprite):
    """Grid with coordinate keys and values
    Player start at "D" if he pick up all items
    he win, else he lose the game"""
    def __init__(self):
        super().__init__()
        """A dict for coordinates
           a list for the way. And a method to set position
           of the objects"""
        self.grid = {}
        self.way_list = []
        self.macGyver = None
        self.guardian = None
        self.inventory = []
        self.readMaze()
        self.setObjects()

    def readMaze(self):
        x, y = 0, 0
        with open("Maze.txt", "r") as line:
            text = line.read()
            for element in text:
                if element == '\n':
                    x, y = 0, y+1
                else:
                    self.grid[(x, y)] = element
                    if element == "0":
                        self.way_list.append((x, y))
                    if element == "D":
                        self.macGyver = x, y
                    if element == "F":
                        self.guardian = x, y
                    x += 1

    def setObjects(self):
        objects = ["T", "S", "E"]
        random.shuffle(self.way_list)
        for key, value in enumerate(objects):
            self.grid[self.way_list[key]] = value

    # DESTINATION
    def checkMove(self, a, b):
        """check the destination"""
        return ((a, b) in self.grid and self.grid[a, b] != "#")

    def checkItems(self, a, b):
        if self.grid[a, b] == "T" or self.grid[a, b] == "S" or self.grid[a, b] == "E":
            self.inventory.append(self.grid[a, b])
            self.grid[a, b] = "0"

    def checkPosGuardian(self, a, b):
        if self.grid[a, b] == self.grid[self.guardian]:
            if len(self.inventory) == 3:
                self.endGame(WIN)
                print("You win")
            else:
                self.endGame(LOSE)
                print("Repose en paix, fils du Gondor.")

    def endGame(self, condition):
        window = pygame.display.set_mode(SIZE)
        bolt_font = pygame.font.SysFont('bolt', 25)
        text_surface = bolt_font.render(condition, True, WHITE)
        text_rect = text_surface.get_rect()
        window.blit(text_surface, text_rect)
        pygame.display.flip()


    # MOVES
    def top(self):
        x = self.macGyver[0]
        y = self.macGyver[1] - 1
        if self.checkMove(x, y):
            self.macGyver = x, y
            self.checkItems(x, y)
            self.checkPosGuardian(x, y)
            # update rect position
            self.rect.x, self.rect.y = x*20, y*20

    def bot(self):
        x = self.macGyver[0]
        y = self.macGyver[1] + 1
        if self.checkMove(x, y):
            self.macGyver = x, y
            self.checkItems(x, y)
            self.checkPosGuardian(x, y)
            # update rect position
            self.rect.x, self.rect.y = x*20, y*20

    def left(self):
        x = self.macGyver[0] - 1
        y = self.macGyver[1]
        if self.checkMove(x, y):
            self.macGyver = x, y
            self.checkItems(x, y)
            self.checkPosGuardian(x, y)
            # update rect position
            self.rect.x, self.rect.y = x*20, y*20

    def right(self):
        x = self.macGyver[0] + 1
        y = self.macGyver[1]
        if self.checkMove(x, y):
            self.macGyver = x, y
            self.checkItems(x, y)
            self.checkPosGuardian(x, y)
            # update rect position
            self.rect.x, self.rect.y = x*20, y*20
