
import pygame
from Configuration import Configurations
from Snake  import  SnakeBlock
from Apple import Apple

def game_event(snake_body: pygame.sprite.Group,
               apples: pygame.sprite.Group) -> bool:
    """
    Función que administra ñps eneventos del juego
    retrun: La bandera del fin del juego
    """

    #Se declara la bandera del fin del juego
    game_over = False

    #Se verifican los eventos de
    for event in pygame.event.get():
        #Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                SnakeBlock.set_is_moving_right(True)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)


            if event.key == pygame.K_LEFT:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(True)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_UP:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(True)
                SnakeBlock.set_is_moving_down(False)

            if event.key == pygame.K_DOWN:
                SnakeBlock.set_is_moving_right(False)
                SnakeBlock.set_is_moving_left(False)
                SnakeBlock.set_is_moving_up(False)
                SnakeBlock.set_is_moving_down(True)

            if event.key == pygame.K_SPACE:
                new_snake_block = SnakeBlock()
                snake_body.add(new_snake_block)

                new_apple = Apple()
                new_apple.random_position()
                apples.add(new_apple)

    #Se regresa la bandera
    return game_over

def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Funcion que gestiona el movimiento del cuerpo de la serpiente

    :param snake_body:
    :return:
    """

    body_size = len(snake_body.sprites()) -1

    for i in range(body_size, 0, -1):
        snake_body.sprites()[i].rect.x = snake_body.sprites()[i-1].rect.x
        snake_body.sprites()[i].rect.y = snake_body.sprites()[i-1].rect.y




    head = snake_body.sprites()[0]

    if SnakeBlock.get_is_moving_right():
        head.rect.x += Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_left():
        head.rect.x -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_up():
        head.rect.y -= Configurations.get_snake_block_size()
    elif SnakeBlock.get_is_moving_down():
        head.rect.y += Configurations.get_snake_block_size()


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock,
                   snake_body: pygame.sprite.Group,
                   apples: pygame.sprite.Group) -> None:
    """
    Función que administrar los elementos visuales del juego
    """
    #Fondo de la pantaña
    screen.fill(Configurations.get_background())

    #Se dibuja el cuerpo de la serpiente
    for snake_block in reversed(snake_body.sprites()):
        snake_block.blit(screen)

    #Se dibuja la manzana
    apples.draw(screen)
    #Se dibuja a la manzana
    #apple.blit(screen)

    pygame.display.flip()

    #Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())
