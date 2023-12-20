import pygame
import elementos2
import random
#iniciamos el juego
pygame.init()

#creamos la pantalla
tamaño = (800,600)
pantalla = pygame.display.set_mode(tamaño)

#reloj
reloj = pygame.time.Clock()
FPS = 60

#booleano de control
running = True
posicion = (200,200)
nave = elementos2.Nave(posicion)

#creamos un grupo de sprites



#grupo_sprites = pygame.sprite.Group(nave)
#grupo_sprites.add(elementos2.Fondo())
#grupo_sprites.add(elementos2.Nave((100,100)))
#grupo_sprites.add(elementos2.Nave((200,100)))
#grupo_sprites.add(elementos2.Nave((300,100)))
grupo_sprites_todos = pygame.sprite.Group()
grupo_sprites_enemigos = pygame.sprite.Group()
grupo_sprites_balas = pygame.sprite.Group()

grupo_sprites_todos.add(elementos2.Fondo((0,0)))
grupo_sprites_todos.add(nave)

enemigo  = elementos2.Enemigo((50,50))
grupo_sprites_enemigos.add(enemigo)

#crear una variable que almacene la ultima vez que se creo un enemigo
ultimo_enemigo_creado = 0
#bucle principal
while running:
    #limitamos el bucle a los FPS definidos
    reloj.tick(FPS)

    #getionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #creacion de enemigos
    coordX = random.randint(0, pantalla.get_width())
    coordY = -200
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + 5000):
        X = random.randint(0, 600)
        enemigo = elementos2.Enemigo((coordX, coordY))
        grupo_sprites_todos.add(enemigo)
        grupo_sprites_enemigos.add(enemigo)
        ultimo_enemigo_creado = momento_actual

    #capturamos las teclas
    teclas = pygame.key.get_pressed()
    #if teclas[pygame.K_SPACE]:
    #    nave.disparar(grupo_sprites_todos)


    #pintaremos
    pantalla.fill((255,255,255))
    grupo_sprites_todos.update(teclas,grupo_sprites_todos, grupo_sprites_balas)
    grupo_sprites_todos.draw(pantalla)

    #redibujar la pantalla 
    pygame.display.flip()

    grupo_sprites_todos.update(teclas, grupo_sprites_todos, grupo_sprites_balas)
    grupo_sprites_todos.draw(pantalla)



#finalizamos el juego 
pygame.quit()