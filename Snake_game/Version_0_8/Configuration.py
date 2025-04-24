class Configurations:
    """
    Clase que contine todas las configuraciones del juego
    """
    #Configuraciones de la pantala
    _screen_size = (1280, 720)
    _game_title = "Snake game en pygame"
    _background = (246, 165, 246)
    _fps = 8 #fps del juego

    #Configuraciones de la serpiente
    #Que sea un divisor común con eñ screen size ⬇️
    _snake_block_size = 80 #Tamaño del bloque de la serpiente
    _snake_head_color = (189, 236, 182)
    _snake_body_color = (157, 214, 173)

    #Configuración de la manzana
    _apple_color = (194, 59, 34)
    _apple_block_size = _snake_block_size


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

    @classmethod
    def get_background(cls) -> tuple[int,int, int]:
        return cls._background

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
    def get_apple_block_size(cls) -> int:
        return cls._apple_block_size
