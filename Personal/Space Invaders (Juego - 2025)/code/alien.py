import pygame
import os

# Obtener el directorio actual del script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)

def get_resource_path(filename):
    """Obtiene la ruta completa de un archivo de recursos"""
    return os.path.join(PARENT_DIR, filename)

class Alien(pygame.sprite.Sprite):
	def __init__(self,color,x,y):
		super().__init__()
		file_path = get_resource_path(f'graphics/{color}.png')
		self.image = pygame.image.load(file_path).convert_alpha()
		self.rect = self.image.get_rect(topleft = (x,y))

		if color == 'red': self.value = 100
		elif color == 'green': self.value = 200
		else: self.value = 300

	def update(self,direction):
		self.rect.x += direction

class Extra(pygame.sprite.Sprite):
	def __init__(self,side,screen_width):
		super().__init__()
		self.image = pygame.image.load(get_resource_path('graphics/extra.png')).convert_alpha()
		
		if side == 'right':
			x = screen_width + 50
			self.speed = - 3
		else:
			x = -50
			self.speed = 3

		self.rect = self.image.get_rect(topleft = (x,80))

	def update(self):
		self.rect.x += self.speed