import pygame
import elementos3
import random
import pygame_menu

#Iniciamos el juego
pygame.init()

#Creamos la pantalla
tamaño = (800, 600)
pantalla = pygame.display.set_mode(tamaño)

#Creamo un reloj para limitar el framerate
reloj = pygame.time.Clock()
FPS = 60

#Booleano de control
running = True

#Creamos la nave
posicion = (360,500)
nave = elementos3.Nave(posicion)

#Creamos un grupo de sprites
# grupo_sprites = pygame.sprite.Group()
# grupo_sprites.add(elementos.Fondo())
# grupo_sprites.add(elementos.Nave((470,100)))
# # grupo_sprites.add(elementos.Nave((200,100)))
# # grupo_sprites.add(elementos.Nave((300,100)))
grupo_sprite_todos = pygame.sprite.Group()
grupo_sprite_enemigos = pygame.sprite.Group()
grupo_sprite_balas = pygame.sprite.Group()

grupo_sprite_todos.add(elementos3.Fondo((0,0)))
grupo_sprite_todos.add(nave)


# enemigo = elementos.Enemigo((50,50))
# grupo_sprites.add(enemigo)
#Creamos una variable que almacena la ultima vez que se creo un enemigo
ultimo_enemigo_creado = 0
frecuencia_creacion_enemigos = 2000
#Creamos el bucle principal
while running:
    #limitamos el bucle al framerate que hemos definido
    reloj.tick(FPS)
    
    #Gestionamos la salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #Creacion de enemigos
    momento_actual = pygame.time.get_ticks()
    if (momento_actual > ultimo_enemigo_creado + frecuencia_creacion_enemigos):
        cordX = random.randint(0, pantalla.get_width())
        cordY = -200
        #Creamos el enemigo y lo añadismos a los grupos.
        enemigo = elementos3.Enemigo((cordX, cordY))
        grupo_sprite_todos.add(enemigo)
        grupo_sprite_enemigos.add(enemigo)
        #Actualizamos el momento del ultimo enemigo creado
        ultimo_enemigo_creado = momento_actual
        
    #Capturamos las teclas
    teclas = pygame.key.get_pressed()
    # if teclas[pygame.K_SPACE]:
    #     nave.disparar(grupo_sprite_todos)
    
    
    #Pintamos
    pantalla.fill((255, 255, 255))
    grupo_sprite_todos.update(teclas, grupo_sprite_todos, grupo_sprite_balas)
    grupo_sprite_todos.draw(pantalla)


    #Redibujar la pantalla
    pygame.display.flip()
    
#Finalizamos el juego
pygame.quit()