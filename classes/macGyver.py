# coding: utf-8

from classes.maze import Maze
import pygame
from settings import PLAYER


class MacGyver(Maze):
    """Hero"""
    def __init__(self):
        super().__init__()
        """Init the object player. Player is a rectangle
        with an image. It's set with attribut self.macGyver * the block size"""
        self.image = pygame.image.load(PLAYER)
        self.rect = self.image.get_rect()
        self.rect.x = self.macGyver[0] * 20
        self.rect.y = self.macGyver[1] * 20
