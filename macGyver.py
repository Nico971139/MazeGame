# coding: utf-8

from maze import Maze
import pygame

class MacGyver(Maze):
	"""Hero"""
	def __init__(self):
		super().__init__()
		"""Init the object player. Player is a rectangle
		with an image. It's set with attribut self.macGyver * the block size"""
		self.image = pygame.image.load('ressource/Mario.png')
		self.rect = self.image.get_rect() #player's position in the game
		self.rect.x = self.macGyver[0] * 20 
		self.rect.y = self.macGyver[1] * 20
