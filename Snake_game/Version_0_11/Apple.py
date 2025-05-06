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

        self._apple_frames = []
        apple_block_size = Configurations.get_apple_size()

        for i in range(len(Configurations.get_apple_images_path())):
            frame = pygame.image.load(Configurations.get_apple_images_path()[i])
            frame = pygame.transform.scale(frame, (apple_block_size, apple_block_size))
            self._apple_frames.append(frame)



        self._last_update_time = pygame.time.get_ticks()
        self._frame_index = 0

        #self.image = pygame.image.load(Configurations.get_apple_image_path()[0])


        self.image = self._apple_frames[self._frame_index]
        self._frame_index = 1

        #self.rect = self.image = pygame.transform.scale(self.image, (apple_block_size, apple_block_size))

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

    def animate_apple(self) -> None:
        """
        Se utiliza para actualizar el frame visible de la manzana
        dando la impresión de movimiento
        :return:
        """
        current_time = pygame.time.get_ticks()
        time_to_refresh = Configurations.get_time_to_refresh()

        #Variable booleana
        needs_refresh = (current_time - self._last_update_time) >= time_to_refresh

        if needs_refresh:
            self.image = self._apple_frames[self._frame_index]

            self._last_update_time = current_time
            self._frame_index += 1

            if self._frame_index >= len(self._apple_frames):
                self._frame_index = 0


    @classmethod
    def get_no_apples(cls) -> int:
        """
        Getter: para no_apples
        :return:
        """
        return cls._no_apples


