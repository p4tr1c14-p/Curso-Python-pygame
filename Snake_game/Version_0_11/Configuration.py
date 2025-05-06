#import pygame.mixer

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    #_background = (246, 165, 246)
    _fps = 4 #fps del juego
    _game_over_screen_time = 1
    _time_to_refresh = 200

    #Configuraciones de la serpiente
    #Que sea un divisor común con eñ screen size ⬇️
    _snake_block_size = 80 #Tamaño del bloque de la serpiente
    _snake_head_color = (189, 236, 182)
    _snake_body_color = (157, 214, 173)

    #Configuración de la manzana
    _apple_color = (194, 59, 34)
    _apple_size = _snake_block_size

    #Las rutas de los archivos multimedia
    _background_image_path = "../media/background_image.jpg"
    _apple_images_path = ["../media/apple1.png",
                         "../media/apple2.png",
                         "../media/apple3.png",
                         "../media/apple4.png"]

    _snake_head_image_path = ["../media/head1.png"
                              "../media/head2.png",
                              "../media/head3.png",
                              "../media/head4.png",
                              "../media/head5.png",
                              "../media/head6.png",
                              "../media/head7.png",
                              "../media/head8.png"]


    _snake_body_image_path = ["../media/body1.png",
                          "../media/body2.png",
                          "../media/body3.png"]


    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title

    """@classmethod
    def get_background(cls) -> tuple[int,int, int]:
        return cls._background"""

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps
    @classmethod
    def get_snake_block_size(cls) -> int:
        return cls._snake_block_size

    @classmethod
    def get_snake_head_color(cls) -> tuple[int, int, int]:
        return cls._snake_head_color

    @classmethod
    def get_snake_body_color(cls) -> tuple[int, int, int]:
        return cls._snake_body_color

#----------------------------------------------------------
    @classmethod
    def get_apple_color(cls) -> tuple[int, int, int]:
        return cls._apple_color

    @classmethod
    def get_apple_size(cls) -> int:
        return cls._apple_size

    @classmethod
    def get_game_over_screen_time(cls) -> int:
        return cls._game_over_screen_time

    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path

    @classmethod
    def get_apple_images_path(cls) -> list:
        return cls._apple_images_path

    @classmethod
    def  get_snake_head_image_path(cls) -> list:
        return cls._snake_head_image_path

    @classmethod
    def get_snake_body_image_path(cls) -> list:
        return cls._snake_body_image_path

    @classmethod
    def get_time_to_refresh(cls) -> int:
        return cls._time_to_refresh

    """@classmethod
    def play_music(cls, volume) -> None:
        pygame.mixer.music.play(loops=-1)  # Él -1 indica que se reproduce
        pygame.mixer.music.set_volume(volume) #En bucle"""
