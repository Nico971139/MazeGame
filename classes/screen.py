# coding: utf-8
import pygame
import sys
from classes.macGyver import MacGyver
from classes.maze import Maze
from settings import (BLOCKS, SIDE, BLACK, TITLE, SIZE, WALL,
 WAY, SYRINGE, ETHER, TUBE, BOSS)

pygame.init()
player = MacGyver()
maze = Maze()


class Screen(object):
    """Attributs of the screen"""
    wall = pygame.image.load(WALL)
    way = pygame.image.load(WAY)
    syringe = pygame.image.load(SYRINGE)
    ether = pygame.image.load(ETHER)
    tube = pygame.image.load(TUBE)
    player_image = player.image
    boss = pygame.image.load(BOSS)
    window = pygame.display.set_mode(SIZE)
    window.fill((BLACK))
    pygame.display.set_caption(TITLE)


def initWaze():
    for y in range(BLOCKS):
        for x in range(BLOCKS):
            if player.grid[(x, y)] == "#":
                Screen.window.blit(Screen.wall, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "0":
                Screen.window.blit(Screen.way, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "D":
                Screen.window.blit(Screen.way, (x * SIDE, y * SIDE))
                Screen.window.blit(Screen.player_image, player.rect)
            if player.grid[(x, y)] == "F":
                Screen.window.blit(Screen.boss, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "T":
                Screen.window.blit(Screen.tube, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "S":
                Screen.window.blit(Screen.syringe, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "E":
                Screen.window.blit(Screen.ether, (x * SIDE, y * SIDE))


def GameStart():
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Screen.window.blit(Screen.way, player.rect)
                    player.right()
                    Screen.window.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_LEFT:
                    Screen.window.blit(Screen.way, player.rect)
                    player.left()
                    Screen.window.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_UP:
                    Screen.window.blit(Screen.way, player.rect)
                    player.top()
                    Screen.window.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_DOWN:
                    Screen.window.blit(Screen.way, player.rect)
                    player.bot()
                    Screen.window.blit(Screen.player_image, player.rect)
                    pygame.display.flip()
        pygame.display.flip()


initWaze()
GameStart()
