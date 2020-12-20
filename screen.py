# coding: utf-8
from maze import *
import pygame, sys
pygame.init()

maze = Maze()
game = Game()
player = MacGyver()
wall = game.wall
way = game.way
player_image = player.image
boss = game.boss_image
# Create the display surface
screen = game.screen
pygame.display.set_caption("MAZE GAME")


x, y = 0, 0
for y in range(15):
	for x in range(15):
		if maze.grid[(x, y)] == "#":
			screen.blit(wall, (x*20, y*20))
		if maze.grid[(x,y)] == "0":
			screen.blit(way, (x*20, y*20))
		if maze.grid[(x,y)] == "D":
			screen.blit(player_image, (x*20, y*20))
		if maze.grid[(x,y)] == "F":
			screen.blit(boss, (x*20, y*20))

# game loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		



	pygame.display.flip()

