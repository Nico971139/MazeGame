# coding: utf-8

import pygame
pygame.init()

#creation de la fenetre de jeu 
pygame.display.set_caption("MAZE GAME")
surface =  pygame.display.set_mode((640, 480))

#fond
background = pygame.image.load('ressource/mountains.jpg')

launched = True
#Boucle du jeu 
while launched:
	# si la fenetre se ferme
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
			pygame.quit()

	surface.blit(background, (0, 0))
	pygame.display.flip()