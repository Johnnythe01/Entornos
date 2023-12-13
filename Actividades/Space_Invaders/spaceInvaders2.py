import pygame
import elementos2

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
posicion = (200,200)
nave = elementos2.Nave(posicion)
# nave = Elementos2.Nave((200,200))

# creamos un grupo de sprites
grupo_sprites = pygame.sprite.Group(nave)
grupo_sprites.add(elementos2.Nave((100,100)))
grupo_sprites.add(elementos2.Nave((300,100)))
grupo_sprites.add(elementos2.Nave((400,100)))

# bucle pricipal
while running:
    # limitamos el bucle a framerate que hemos definido
    reloj.tick(FPS)

    # gestionar la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #capturamos las teclas
    teclas = pygame.key.get_pressed()

    # pintaremos
    # primero el fondo blanco
    pantalla.fill((255,255,255))
    # segundo los sprites
    grupo_sprites.update(teclas)
    grupo_sprites.draw(pantalla)

    # redibujar la pantalla
    pygame.display.flip()

# finalizamos el juego
pygame.quit()