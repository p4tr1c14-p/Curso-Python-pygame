import time

import pygame
from Configuration import Configurations
from Snake  import  SnakeBlock
from Apple import Apple

def game_event() -> bool:
    """
    Función que administra ñps eventos del juego
    return: La bandera del fin del juego
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

                #new_apple = Apple()
                #new_apple.random_position(snake_body)
                #print(Apple.get_no_apples())

                #apples.remove(apples.sprites()[0])
                #apples.empty()
                #apples.add(new_apple)

    #Se regresa la bandera
    return game_over

def snake_movement(snake_body: pygame.sprite.Group) -> None:
    """
    Función que gestiona el movimiento del cuerpo de la serpiente

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

def check_collision(screen: pygame.surface.Surface,
                    snake_body: pygame.sprite.Group,
                    apples: pygame.sprite.Group)-> bool:
    """
    Función que revisa las coliciones del juego
    Cabeza de la serpiente con el cuerpo
    Cabeza de la serpiente con el borde de la pantalla
    Cabeza de la serpiente con el borde de la manzana
    :param screen: Pantalla
    :param snake_body: Cuerpo de la serpiente
    :param apples: Grupo de las manzanas
    :return:
    """
    #Se declara la bandera del fin del juego
    game_over = False

    #Se obtiene la cabeza de la serpiente
    head = snake_body.sprites()[0]

    #Se revisa la condición de cabeza de
    # la serpiente con el borde de la pantalla
    screen_rect = screen.get_rect()

    if head.rect.right > screen_rect.right or head.rect.left < screen_rect.left or head.rect.bottom > screen_rect.bottom or head.rect.top < screen_rect.top:
        game_over = True

    #Se revisan las condiciones de la cabeza de la serpiente con su cuerpo
    head_body_collisions = pygame.sprite.spritecollide(head, snake_body, dokill=False)

    if len(head_body_collisions) > 1:
        game_over = True


    head_apple_collisions = pygame.sprite.spritecollide(head, apples, dokill= True)
    if len(head_apple_collisions) > 0:
        new_snake_block = SnakeBlock()
        new_snake_block.rect.x = snake_body.sprites()[-1].rect.x
        new_snake_block.rect.y = snake_body.sprites()[-1].rect.y
        snake_body.add(new_snake_block)

        new_apple = Apple()
        new_apple.random_position(snake_body)
        apples.add(new_apple)

    return game_over



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

def game_over_screen() -> None:
    """
    Función con la parte del fin del juego
    :return:
    """
    time.sleep(Configurations.get_game_over_screen_time())