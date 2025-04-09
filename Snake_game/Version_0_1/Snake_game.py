"""
Nombre: Patricia Pérez Cruz
Fecha: 08/04/2025
Version 0.1:
-Se crea la pantalla de inicio
-Se configura el título de la pantalla
"""
import pygame

def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Se inicializa el módulo pygame
    pygame.init()

    #Se inicializa la pantalla
    screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size )

    #Se configura el título del juego
    game_title = "Snake gae en pygame"
    pygame.display.set_caption(game_title)

    #Ciclo principal de videojuego
    game_over = False

    while not game_over:
        #Se verifican los eventos (teclado y ratón) del juego
        for event in pygame.event.get():
            #Un clic en cerrar el juego
            if event.type == pygame.QUIT: #Evento cerrar ventana
                game_over = True

            #Se dibujan los elementos gráficos en la pantalla
            background = (234, 137, 154) #Fondo de la pantalla en formato RGB
            screen.fill(background)

            #Se actualiza la pantalla
            pygame.display.flip()

    pygame.quit() #Cerrar recursos

if __name__ == '__main__':
    run_game()