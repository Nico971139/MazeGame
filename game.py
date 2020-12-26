# coding: utf-8

import pygame

class Game():
	""" Game display """
	def __init__(self):
		"""Attributes of the game screen """
		self.size = self.width, self.height = 300, 300
		self.screen = pygame.display.set_mode(self.size)
		self.wall = pygame.image.load('ressource/mur.png')
		self.way = pygame.image.load('ressource/chemin.png')
		self.boss_image = pygame.image.load('ressource/gardien.png')
		self.syringe = pygame.image.load('ressource/seringue.png')
		self.ether = pygame.image.load('ressource/ether.png')
		self.tube = pygame.image.load('ressource/tube.png')	
	
