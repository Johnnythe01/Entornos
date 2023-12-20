import pygame
import elementos2
import random

# inicializamos el juego
pygame.init()

# creamos la pantalla
tamano = (800, 600)
pantalla = pygame.display.set_mode(tamano)

# creamos un reloj
reloj = pygame.time.Clock()
FPS = 60

# booleano de control
running = True

nave = elementos2.Nave((400,500))
# nave = Elementos2.Nave((200,200))

# creamos un grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementos2.Nave((100,100)))
grupo_sprites.add(elementos2.Nave((420,100)))
grupo_sprites.add(elementos2.Nave((300,100)))

grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_balas = pygame.sprite.Group()

grupo_sprites_todos.add(elementos2.Fondo((0,0)))
grupo_sprites_todos.add(nave)

enemigo = elementos2.Enemigo((50,50))
grupo_sprites.add(enemigo)

#crear una variable que almacene la última vez que se creó un enemigo
ultimo_enemigo_creado = 0

# bucle pricipal
while running:
    # limitamos el bucle a framerate que hemos definido
    reloj.tick(FPS)

    # gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creacion de enemigos
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + 6000):
        coordX = random.randint(0,pantalla.get_width())
        coordY = -200
        # creamos el enemigo
        grupo_sprites_todos.add(enemigo)
        # lo añadimos a los dos grupos: todos y enemigos
        grupo_sprites.add(elementos2.Enemigo((coordX, coordY)))
        grupo_sprites_enemigos.add(enemigo)
        # actualizamos el momento del último enemigo creado
        ultimo_enemigo_creado = momento_actual
    

    #capturamos las teclas
    teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_SPACE]:
    #     nave.disparar(grupo_sprites_todos)

    # pintaremos
    # primero el fondo blanco
    pantalla.fill((255,255,255))

    # segundo los sprites
    grupo_sprites.update(teclas,grupo_sprites_todos,grupo_sprites_balas)
    grupo_sprites.draw(pantalla)
    grupo_sprites_todos

    # redibujar la pantalla
    pygame.display.flip()

# finalizamos el juego
pygame.quit()