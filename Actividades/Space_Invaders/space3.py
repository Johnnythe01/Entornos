import pygame
import elementos3
import random
# Iniciamos el juego
pygame.init()

# Creamos la pantalla
tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

# Reloj
reloj = pygame.time.Clock()
FPS = 60

# Booleano de control
running = True

# Creamos la nave
posicion = (200,200)
nave = elementos3.Nave(posicion)

# Creamos un grupo de sprites

#grupo_sprites = pygame.sprite.Group(nave)
#grupo_sprites.add(elementos2.Fondo())
#grupo_sprites.add(elementos2.Nave((100,100)))
#grupo_sprites.add(elementos2.Nave((200,100)))
#grupo_sprites.add(elementos2.Nave((300,100)))
grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_balas = pygame.sprite.Group()

grupo_sprites_todos.add(elementos3.Fondo((0,0)))
grupo_sprites_todos.add(nave)

enemigo  = elementos3.Enemigo((50,50))
grupo_sprites_enemigos.add(enemigo)

# Crear una variable que almacene la ultima vez que se creo un enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigos = 2000
# Bucle principal
while running:
    # Limitamos el bucle a los FPS definidos
    reloj.tick(FPS)

    # Gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Creacion de enemigos
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigos):
        coordX = random.randint(0, pantalla.get_width())
        coordY = -200
        # Creamos el enemigo y lo añadimos a los grupos.
        enemigo = elementos3.Enemigo((coordX, coordY))
        grupo_sprites_todos.add(enemigo)
        grupo_sprites_enemigos.add(enemigo)
        # Actualizamos el momento del ultimo enemigo creado.
        ultimo_enemigo_creado = momento_actual

    # Capturamos las teclas
    teclas = pygame.key.get_pressed()
    #if teclas[pygame.K_SPACE]:
    #    nave.disparar(grupo_sprites_todos)

    # Pintaremos
    pantalla.fill((255,255,255))

    grupo_sprites_todos.update(teclas,grupo_sprites_todos, grupo_sprites_balas)
    grupo_sprites_todos.draw(pantalla)

    # Redibujar la pantalla 
    pygame.display.flip()

# Finalizamos el juego 
pygame.quit()