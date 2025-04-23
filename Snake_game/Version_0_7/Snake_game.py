"""
Nombre: Patricia Pérez Cruz
Fecha: 08/04/2025
Version 02:
-Se agregó la clase Configurations en el módulo Configurations.py que va a incluir todas las
configuraciones del juego
-Se agregó el módul Game funcine que admiistra los eve
-Se agregaa
"""
import pygame
from Configuration import Configurations
from Game_Functionalities import game_event, screen_refresh, snake_movement
from Snake import  SnakeBlock
from pygame.sprite import Group
from Apple import Apple


def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()
    #Se configur EL RELOJ DEL JUEGO
    clock = pygame.time.Clock()

    #Se inicializa la pantalla
    screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size)
    #screen = pygame.display.set_mode(Configurations.get_screen_size() )

    #Se configura el título del juego
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())
    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock(is_head= True)
    snake_head.snake_head_init()

    #Se crea un grupo para almacenar el cuerpo de la serpiente
    snake_body = Group()
    snake_body.add(snake_head)

    #Se crea el bloque inicial de la manzana
    apple = Apple()
    apple.random_position()

    #Se crea grupo
    apples = Group()
    apples.add(apple)

    #Ciclo principal de videojuego
    game_over = False

    while not game_over:
        game_over = game_event(snake_body, apples)

        #Se administra el movimiento de la serpiente
        snake_movement(snake_body)

        #Se dibujan los elementos gráficos en la pantalla
        screen_refresh(screen, clock, snake_body, apples)

#Se cierran los eventos
pygame.quit()

if __name__ == '__main__':
    run_game()