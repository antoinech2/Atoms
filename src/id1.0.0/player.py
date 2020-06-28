import pygame
import random
import math
#import main
from os import chdir
chdir('C:/Antoine/Programmation/Python/pygame/atomes/src/id1.0.0')

class Player(pygame.sprite.Sprite):

	DIR_NORTH = 0
	DIR_NORTH_EAST = 1
	DIR_EAST = 2
	DIR_SOUTH_EAST = 3
	DIR_SOUTH = 4
	DIR_SOUTH_WEST = 5
	DIR_WEST = 6
	DIR_NORTH_WEST = 7

	def __init__(self, type):
		super().__init__()
		if type == "hydrogen":
			self.image = pygame.transform.scale(pygame.image.load("../../res/textures/player/atome-hydrogene.png"), (53, 53))
		else:
			self.image = pygame.transform.scale(pygame.image.load("../../res/textures/player/atome-oxygene.png"), (60, 60))
		self.rect = self.image.get_rect()
		self.rect.x = random.randint(200,1300)
		self.rect.y = random.randint(200,1300)
		self.vitesse = 1
		self.type = type

	def Move(self, atoms):
		for loop in atoms:
			if loop != self:
				angle = math.atan2(loop.rect.y-self.rect.y, loop.rect.x-self.rect.x)
				self.rect.x += math.cos(angle)*self.vitesse
				self.rect.y += math.sin(angle)*self.vitesse
				print(loop.rect.y-self.rect.y, loop.rect.x-self.rect.x)
				#self.rect.x += random.randint(-5,5)
				#self.rect.y += random.randint(-5,5)
