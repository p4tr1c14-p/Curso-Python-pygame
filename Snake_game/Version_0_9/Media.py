import pygame
from Configuration import Configurations

class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image, self.rect)

"""class Applee:
    def __init__(self):
        
        apple_image_path = Configurations.get_apple1_image_path()
        self.image = pygame.image.load(apple_image_path)
        

        self.image = pygame.image.load(Configurations.get_apple1_image_path())
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        screen.blit(self.image, self.rect)"""

"""

        apple_image_path = Configurations.get_apple1_image_path()
        self.image = pygame.image.load(apple_image_path)

        #Se escala la imagen al tamaño de la pantalla
        apple_size = Configurations.get_apple_block_size()
        self.image = pygame.transform.scale(self.image, apple_size)

        self.rect = self.image.get_rect()

        #Se escala la manzana 🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎
        apple_size = Configurations.get_apple_block_size()
        self.image = pygame.transform.scale(self.image, apple_size)

        self.rect = self.image.get_rect()"""





