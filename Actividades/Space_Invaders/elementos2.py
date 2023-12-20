from typing import Any
import pygame
from pygame.sprite import Group, Group

class Nave(pygame.sprite.Sprite):
    # constructor
    def __init__(self, posicion):
        super().__init__()
        # cargamos la imagen
        self.manolos = pygame.image.load("avion.png"), pygame.image.load("avion2.png")
        #imagen = (pygame.image.load("avion.png"), pygame.image.load("avion2.png"))
        self.indice_manolos = 0
        self.image = self.manolos [self.indice_manolos]
        self.contador_imagen = 0
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
        self.ultimo_disparo = 0

        # update
    def update(self, *args: any, **kwargs: any):
        #capturamos las teclas
        teclas = args[0]
        # capturamos grupo_sprites_todos
        grupo_sprites_todos = args [1]
        # capturamos grupo_sprites_
        grupo_sprites_balas = args [2]
        # capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
            pantalla = pygame.display.get_surface()
        if teclas[pygame.K_RIGHT]:
            self.rect.x += 2
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x, )
            pantalla = pygame.display.get_surface()
        if teclas[pygame.K_SPACE]:
        # disparar
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)
        # gestionamos la animacion
        self.contador_imagen = (self.contador_imagen +1) % 40
        self.indice_manolo = self.contador_imagen // 20
        self.image = self.manolos[self.indice_manolo]
            
        if teclas[pygame.K_UP]:
            self.rect.y -= 2
        if teclas[pygame.K_DOWN]:
            self.rect.y += 2

            pantalla = pygame.display.get_surface()
        if (self.rect.y > pantalla.get_height() -200):
            self.kill()

        #capturar el arg[2] -> grupo_sprites_balas
        grupo_sprites_balas = args [2]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprites_balas)
        if bala_colision:
            self.kill()
            bala_colision.kill()
    def disparar(self, grupo_sprites_todos, grupo_sprites_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimo_disparo + 200:
            bala = Bala(
                (self.rect.x + self.image.get_width() /2, self.rect.y))
        grupo_sprites_todos.add(bala)
        grupo_sprites_balas.add(bala)
        self.ultimo_disparo = momento_actual

class Fondo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        # cargamos la imagen
        imagen_cargada = pygame.image.load("space.jpg")
        # capturamos la pantalla
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(
            imagen_cargada, (pantalla.get_width(), pantalla.get_height()))
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = (0,0)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__
        # creamos un rectangulo
        self.image = pygame.Surface((5,10))
        self.image.fill ((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.y -= 5

class Enemigo(pygame.sprite.Sprite):
    # constructor
    def __init__(self, posicion):
        super().__init__()
        # cargamos la imagen
        manolo = pygame.image.load("avion.png")
        self.image = pygame.transform.rotate(manolo, 180)
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion
            
    def update(self, *args: any, **kwargs: any):
        self.rect.y += 1