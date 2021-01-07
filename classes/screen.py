# coding: utf-8
import pygame
import sys
from classes.macGyver import MacGyver
from settings import (BLOCKS, SIDE, BLACK, TITLE, SIZE, WALL,
WAY, SYRINGE, ETHER, TUBE, BOSS)

pygame.init()
player = MacGyver()


class Screen():
    """Attributs of the screen"""
    def __init__(self):
        self.wall = pygame.image.load(WALL)
        self.way = pygame.image.load(WAY)
        self.syringe = pygame.image.load(SYRINGE)
        self.ether = pygame.image.load(ETHER)
        self.tube = pygame.image.load(TUBE)
        self.player_image = player.image
        self.boss = pygame.image.load(BOSS)
        self.window = pygame.display.set_mode(SIZE)
        self.window.fill((BLACK))
        pygame.display.set_caption(TITLE)
        self.initWaze()
        self.GameStart()

    def initWaze(self):
        for y in range(BLOCKS):
            for x in range(BLOCKS):
                if player.grid[(x, y)] == "#":
                    self.window.blit(self.wall, (x * SIDE, y * SIDE))
                if player.grid[(x, y)] == "0":
                    self.window.blit(self.way, (x * SIDE, y * SIDE))
                if player.grid[(x, y)] == "D":
                    self.window.blit(self.way, (x * SIDE, y * SIDE))
                    self.window.blit(self.player_image, player.rect)
                if player.grid[(x, y)] == "F":
                    self.window.blit(self.boss, (x * SIDE, y * SIDE))
                if player.grid[(x, y)] == "T":
                    self.window.blit(self.tube, (x * SIDE, y * SIDE))
                if player.grid[(x, y)] == "S":
                    self.window.blit(self.syringe, (x * SIDE, y * SIDE))
                if player.grid[(x, y)] == "E":
                    self.window.blit(self.ether, (x * SIDE, y * SIDE))

    def GameStart(self):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.window.blit(self.way, player.rect)
                        player.right()
                        self.window.blit(self.player_image, player.rect)
                        pygame.display.flip()

                    elif event.key == pygame.K_LEFT:
                        self.window.blit(self.way, player.rect)
                        player.left()
                        self.window.blit(self.player_image, player.rect)
                        pygame.display.flip()

                    elif event.key == pygame.K_UP:
                        self.window.blit(self.way, player.rect)
                        player.top()
                        self.window.blit(self.player_image, player.rect)
                        pygame.display.flip()

                    elif event.key == pygame.K_DOWN:
                        self.window.blit(self.way, player.rect)
                        player.bot()
                        self.window.blit(self.player_image, player.rect)
                        pygame.display.flip()
            pygame.display.flip()
