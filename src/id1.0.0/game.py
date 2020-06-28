import pygame
from player import Player
import random

class Game:
	def __init__(self):
		pygame.init()
		#Initialisation de la fenêtre
		self.screen_size = (1500,1000)
		self.screen = pygame.display.set_mode(self.screen_size)
		pygame.display.set_caption("Jeu de test")

		self.is_running = True

		self.background_color = pygame.Color("white")

		self.all_atoms = pygame.sprite.Group()
		self.all_atoms.add(Player("hydrogen"))
		self.all_atoms.add(Player("oxygen"))
		#self.hydrogen = Player("hydrogen")
		#self.oxygen = Player("oxygen")

	def Start(self):
		while self.is_running:
			self.screen.fill(self.background_color)
			#self.screen.blit(self.oxygen.GetImage(), self.oxygen.GetRect())
			#self.screen.blit(self.hydrogen.GetImage(), self.hydrogen.GetRect())
			self.all_atoms.draw(self.screen)

			#self.oxygen.Move()
			#self.hydrogen.Move()
			for atom in self.all_atoms:
				atom.Move(self.all_atoms)
			pygame.display.update()

			# rand = random.randint(0,1)
			# if rand == 0:
			# 	for atom in range (150):
			# 		if random.randint(0,1) == 0:
			# 			self.all_atoms.add(Player("oxygen"))
			# 		else:
			# 			self.all_atoms.add(Player("hydrogen"))
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.Stop()
		pygame.quit()
	def Stop(self):
		self.is_running = False
