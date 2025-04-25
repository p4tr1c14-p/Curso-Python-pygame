"""
Nombre: Patricia Pérez Cruz
Fecha: 08/04/2025
Version 08:
-Se verifican coliciones
"""
import pygame
from Configuration import Configurations
from Game_Functionalities import game_event, screen_refresh, snake_movement, check_collision, game_over_screen
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
    apple.random_position(snake_body)

    #Se crea grupo
    apples = Group()
    apples.add(apple)

    #Ciclo principal de videojuego
    game_over = False

    while not game_over:
            game_over = game_event()
            #Condición de que cerró la ventaa
            if game_over:
                break

            #Se administra el movimiento de la serpiente
            snake_movement(snake_body)

            #Se revisan las coliciones en el juego
            game_over = check_collision(screen, snake_body, apples)

            # Se dibujan los elementos gráficos en la pantalla
            screen_refresh(screen, clock, snake_body, apples)

            #Si ha perdido el jugador se llama a la pantalla del fin del juego
            if game_over:
                game_over_screen()



#Se cierran los eventos
    pygame.quit()

if __name__ == '__main__':
    run_game()