# coding: utf-8
from maze import Maze, Game, MacGyver
import pygame, sys
pygame.init()

game = Game()
player = MacGyver()
wall = game.wall
way = game.way
syringe = game.syringe
ether = game.ether
tube = game.tube
player_image = player.image
player_rect = player_image.get_rect()
boss = game.boss_image
# Create the display surface
screen = game.screen
pygame.display.set_caption("MAZE GAME")


x, y = 0, 0
""" x = absciss on screen 
	y = ordinate on screen
	20 = size of block """
for y in range(15):
	for x in range(15):
		if player.grid[(x, y)] == "#":
			screen.blit(wall, (x*20, y*20))
		if player.grid[(x,y)] == "0":
			screen.blit(way, (x*20, y*20))
		if player.grid[(x,y)] == "D":
			screen.blit(way, (x*20, y*20))
			screen.blit(player_image, player.rect)
		if player.grid[(x,y)] == "F":
			screen.blit(boss, (x*20, y*20))
		if player.grid[(x, y)] == "T":
			screen.blit(tube, (x*20,y*20))
		if player.grid[(x, y)] == "S":
			screen.blit(syringe, (x*20,y*20))
		if player.grid[(x, y)] == "E":
			screen.blit(ether, (x*20,y*20))
# game loop
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				player.right()
				screen.blit(player_image, player.rect)
				pygame.display.flip()
			elif event.key == pygame.K_LEFT:
				player.left()
				screen.blit(player_image, player.rect)
				pygame.display.flip()
			elif event.key == pygame.K_UP:
				player.top()
				screen.blit(player_image, player.rect)
				pygame.display.flip() 
			elif event.key == pygame.K_DOWN:
				player.bot()
				screen.blit(player_image, player.rect)
				pygame.display.flip()



	pygame.display.flip()

