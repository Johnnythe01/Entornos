import pygame
from pygame.sprite import Group

class Nave(pygame.sprite.Sprite):
    # constructor
    def __init__(self, posicion):
        super().__init__()
        # cargamos la imagen
        self.manolos = pygame.image.load("avion.png"), pygame.image.load("avion2.png")
        imagen = (pygame.image.load("avion.png"), pygame.image.load("avion2.png"))
        self.indice_manolos = 0
        self.image = self.manolos [self.indice_manolos]
        self.contador_imagen = 0
        # creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # actualizar la posicion del rectangulo para que coincida con "posicion"
        self.rect.topleft = posicion

        # update
    def update(self, *args: any, **kwargs: any):
        #capturamos las teclas
        teclas = args[0]
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
        # gestionamos la animacion
        self.contador_imagen = (self.contador_imagen +1) % 40
        self.indice_manolo = self.contador_imagen //20
        self.image = self.manolos[self.indice_manolo]
            
        if teclas[pygame.K_UP]:
            self.rect.y -= 2
        if teclas[pygame.K_DOWN]:
            self.rect.y += 2


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