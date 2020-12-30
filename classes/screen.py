# coding: utf-8
import pygame
import sys
from classes.macGyver import MacGyver
from settings import (BLOCKS, SIDE, BLACK, TITLE, SIZE,
WALL, WAY, SYRINGE, ETHER, TUBE, BOSS)

pygame.init()
player = MacGyver()


class Screen(object):
    """docstring for Screen"""
    wall = pygame.image.load(WALL)
    way = pygame.image.load(WAY)
    syringe = pygame.image.load(SYRINGE)
    ether = pygame.image.load(SYRINGE)
    tube = pygame.image.load(TUBE)
    player_image = player.image
    boss = pygame.image.load(BOSS)
    screen = pygame.display.set_mode(SIZE)
    screen.fill((BLACK))
    pygame.display.set_caption(TITLE)


def draw_waze():
    for y in range(BLOCKS):
        for x in range(BLOCKS):
            if player.grid[(x, y)] == "#":
                Screen.screen.blit(Screen.wall, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "0":
                Screen.screen.blit(Screen.way, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "D":
                Screen.screen.blit(Screen.way, (x * SIDE, y * SIDE))
                Screen.screen.blit(Screen.player_image, player.rect)
            if player.grid[(x, y)] == "F":
                Screen.screen.blit(Screen.boss, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "T":
                Screen.screen.blit(Screen.tube, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "S":
                Screen.screen.blit(Screen.syringe, (x * SIDE, y * SIDE))
            if player.grid[(x, y)] == "E":
                Screen.screen.blit(Screen.ether, (x * SIDE, y * SIDE))


def launch_game():
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Screen.screen.blit(Screen.way, player.rect)
                    player.right()
                    Screen.screen.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_LEFT:
                    Screen.screen.blit(Screen.way, player.rect)
                    player.left()
                    Screen.screen.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_UP:
                    Screen.screen.blit(Screen.way, player.rect)
                    player.top()
                    Screen.screen.blit(Screen.player_image, player.rect)
                    pygame.display.flip()

                elif event.key == pygame.K_DOWN:
                    Screen.screen.blit(Screen.way, player.rect)
                    player.bot()
                    Screen.screen.blit(Screen.player_image, player.rect)
                    pygame.display.flip()
        pygame.display.flip()


draw_waze()
launch_game()
