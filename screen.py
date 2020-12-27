# coding: utf-8
from maze import Maze
from macGyver import MacGyver
from game import Game
from setting import *
import pygame, sys

pygame.init()

game = Game()
player = MacGyver()

# Create the display surface
screen = game.screen
screen.fill((black))
pygame.display.set_caption("MAZE GAME")


def draw_waze():
	for y in range(15):
		for x in range(15):
			if player.grid[(x, y)] == "#":
				screen.blit(wall, (x * 20, y * 20))
			if player.grid[(x,y)] == "0":
				screen.blit(way, (x * 20, y * 20))
			if player.grid[(x,y)] == "D":
				screen.blit(way, (x * 20, y * 20))
				screen.blit(player_image, player.rect)
			if player.grid[(x,y)] == "F":
				screen.blit(boss, (x * 20,y * 20))
			if player.grid[(x, y)] == "T":
				screen.blit(tube, (x * 20, y * 20))
			if player.grid[(x, y)] == "S":
				screen.blit(syringe, (x * 20,y * 20))
			if player.grid[(x, y)] == "E":
				screen.blit(ether, (x * 20, y* 20))


# game loop
def launch_game():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					screen.blit(way, player.rect)
					player.right()
					screen.blit(player_image, player.rect)
					pygame.display.flip()
				elif event.key == pygame.K_LEFT:
					screen.blit(way, player.rect)
					player.left()	
					screen.blit(player_image, player.rect)
					pygame.display.flip()
				elif event.key == pygame.K_UP:
					screen.blit(way, player.rect)
					player.top()
					screen.blit(player_image, player.rect)
					pygame.display.flip() 
				elif event.key == pygame.K_DOWN:
					screen.blit(way, player.rect)
					player.bot()
					screen.blit(player_image, player.rect)
					pygame.display.flip()
		pygame.display.flip()


draw_waze()
launch_game()