import pygame
import sys
from pygame.locals import *

## COLORS ##

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
COMBLUE  = (233, 232, 255)

BGCOLOR = BLACK

class App(object):
	def __init__(self):
		pygame.init()
		self.displaySurf = self.makeScreen()   #, self.displayRect


	def makeScreen(self):
		pygame.display.set_caption('Arkanoid') #define um titulo
		displaySurf = pygame.display.set_mode((300,400)) #cria uma tela
		displaySurf.fill(BGCOLOR)  #colore o background
		#displayRect = displaySurf.get_rect()
		return displaySurf

	def mainLoop(self):
		while True: # main game loop
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
					


if __name__ == '__main__':

	runGame = App()
	runGame.mainLoop()