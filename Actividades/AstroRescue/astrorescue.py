import pygame
import rescElementos
import random
#import pygame_menu

# Iniciamos el juego
pygame.init()

# Creamos la pantalla
tamaño = (800, 600)
pantalla = pygame.display.set_mode(tamaño)

# Creamos la puntuacion
puntuacion = 0

# Creamos un reloj para limitar el framerate
reloj = pygame.time.Clock()
FPS = 60

# Booleano de control
running = True

# Creamos la nave
posicion = (360,540)
nave = rescElementos.Nave(posicion)

# Creamos un grupo de sprites
#grupo_sprites = pygame.sprite.Group()
#grupo_sprites.add(rescElementos.Fondo())
#grupo_sprites.add(rescElementos.Nave((470,100)))
#grupo_sprites.add(rescElementos.Nave((200,100)))
#grupo_sprites.add(rescElementos.Nave((300,100)))
grupo_sprite_todos = pygame.sprite.Group()
grupo_sprite_enemigos = pygame.sprite.Group()
grupo_sprite_balas = pygame.sprite.Group()

grupo_sprite_todos.add(rescElementos.Fondo((0,0)))
grupo_sprite_todos.add(nave)  

enemigo = rescElementos.Enemigo((50,50))
grupo_sprite_todos.add(enemigo)
grupo_sprite_enemigos.add(enemigo)
# Creamos una variable que almacena la ultima vez que se creo un enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigos = 2000
# Creamos el bucle principal
while running:
    # limitamos el bucle al framerate que hemos definido
    reloj.tick(FPS)
    
    # Gestionamos la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar colisiones entre la nave y los enemigos
    nave.detectar_colisiones_nave_enemigos(grupo_sprite_enemigos)

    # Detectar colisiones entre balas y enemigos
    colisiones_balas_enemigos = pygame.sprite.groupcollide(grupo_sprite_balas, grupo_sprite_enemigos, True, True)

    # Actualizar la puntuación por cada enemigo eliminado por una bala
    for bala, enemigos in colisiones_balas_enemigos.items():
        puntuacion += len(enemigos) * 100

        # Si nos eliminan, acaba la partida automáticamente
    if nave.vida <= 0:
        running = False

    # Creacion de enemigos
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigos):
        cordX = random.randint(0, pantalla.get_width())
        cordY = -200
        # Creamos el enemigo y lo añadimos a los grupos.
        enemigo = rescElementos.Enemigo((cordX, cordY))
        grupo_sprite_todos.add(enemigo)
        grupo_sprite_enemigos.add(enemigo)

        # Actualizamos el momento del ultimo enemigo creado
        ultimo_enemigo_creado = momento_actual
        
    # Capturamos las teclas
    teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_SPACE]:
    #     nave.disparar(grupo_sprite_todos)
    
    # Pintamos
    pantalla.fill((255, 255, 255))
    grupo_sprite_todos.update(teclas, grupo_sprite_todos, grupo_sprite_balas,grupo_sprite_enemigos)
    grupo_sprite_todos.draw(pantalla)

    # Dibujar la puntuación en la pantalla
    fuente = pygame.font.Font(None, 36)
    texto_puntuacion = fuente.render("Puntuación: " + str(puntuacion), True, (255, 255, 255))
    pantalla.blit(texto_puntuacion, (10, 10))  

    # Redibujar la pantalla
    pygame.display.flip()
    
# Finalizamos el juego
pygame.quit()