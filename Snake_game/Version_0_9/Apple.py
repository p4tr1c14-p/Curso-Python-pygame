import pygame
from pygame.sprite import Sprite
from Configuration import Configurations
from random import randint

class Apple(Sprite):

    #Atributo de clase para la puntuación
    _no_apples = 0

    def __init__(self) -> None:
        super().__init__()

        Apple._no_apples += 1
       #screen = pygame.display.set_mode(Configurations.get_screen_size())

        #_apple_block_size = Configurations.get_apple_block_size()
        self.image = pygame.Surface((Configurations.get_apple_size(), Configurations.get_apple_size()))
        self.image.fill(color=Configurations.get_apple_color())

        #self.image = pygame.Surface()

        self.rect = self.image.get_rect()

    def blit(self, screen : pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)

    def random_position(self, snake_body: pygame.sprite.Group) -> None:
        """
        Se utiliza para inicializar una ubicación aleatoria de la manzana
        y verificar que no se sobreponga en el cuerpo de la serpiente
        """
        repeat = True
        while repeat:
            #Se genera la posición aleatoria
            screen_width = Configurations.get_screen_size()[0]
            screen_height = Configurations.get_screen_size()[1]
            apple_size = Configurations.get_apple_size()

            self.rect.x = apple_size * randint(0, (screen_width // apple_size - 1))
            self.rect.y = apple_size * randint(0, (screen_height // apple_size - 1))

            #Se verifica que no se encuentre sobre el cuerpo de la serpiente
            for snake_block in snake_body.sprites():
                if self.rect == snake_block.rect:
                    repeat = True
                    break
                else:
                    repeat = False
    @classmethod
    def get_no_apples(cls) -> int:
        """
        Getter: para no_apples
        :return:
        """
        return cls._no_apples


