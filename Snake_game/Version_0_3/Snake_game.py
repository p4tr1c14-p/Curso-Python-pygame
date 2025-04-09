"""
Nombre: Patricia Pérez Cruz
Fecha: 08/04/2025
Version 02:
-Se agregó la clase Configurations en el módulo Cnfigurations.py que va a incluir todas las
configuraciones del juego
-Se agregó el módul Game funcine que admiistra los eve
"""
import pygame
from Configuration import Configurations
from Game_Functionalities import game_event, screen_refresh
from Snake import  SnakeBlock


def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()

    #Se inicializa la pantalla
    #screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size() )

    #Se configura el título del juego
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())
    #Se crea el bloque inicial de la serpiente (cabeza)
    snake_head = SnakeBlock()

    #Ciclo principal de videojuego
    game_over = False

    while not game_over:
        game_over = game_event()

        screen_refresh(screen, snake_head)
#Se cierran los eventos
pygame.quit()

if __name__ == '__main__':
    run_game()