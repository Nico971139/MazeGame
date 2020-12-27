# coding: utf-8
from maze import Maze
from macGyver import MacGyver
from game import Game
import pygame

###########################
#		ENVIRONMENT       #
###########################
player = MacGyver()
game = Game()
wall = game.wall
way = game.way
syringe = game.syringe
ether = game.ether
tube = game.tube
player_image = player.image
boss = game.boss_image

###########################
#		COLOR SET		  #
###########################

black = (0, 0, 0)
white = (240, 240, 240)