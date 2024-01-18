import pygame

class Nave(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()

        imagen = [pygame.image.load("avion.png"), pygame.image.load("avion2.png"), ]
        self.imagennave = [pygame.transform.scale(imagen[0], (60, 60)), pygame.transform.scale(imagen[1], (60, 60))]
        self.indicenave = 0
        self.image = self.imagennave[self.indicenave]
        self.contador_imagen = 0
        self.rect = self.image.get_rect()
        #actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.center = posicion
        self.ultimoDisparo = 0
    
    #update
    def update(self, *args: any, **kwargs: any):
        teclas = args[0]
        #capturamos grupo sprites todos
        grupo_sprites_todos = args[1]
        #capturamos grupo sprites balas 
        grupo_sprites_balas = args[2]
        if teclas[pygame.K_LEFT]:
            Nave.moverIzquierda(self)
        if teclas[pygame.K_RIGHT]:
            Nave.moverDerecha(self)
        if teclas[pygame.K_UP]:
            Nave.moverArriba(self)
        if teclas[pygame.K_DOWN]:
            Nave.moverAbajo(self)
        #gestionamos la animación
        self.contador_imagen = (self.contador_imagen + 1) % 40
        self.indicenave = self.contador_imagen // 20
        self.image = self.imagennave[self.indicenave]
        if teclas[pygame.K_SPACE]:
            #disparar
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)

       

    def moverDerecha(self):
        self.rect.x += 2
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.rect.x = min(limite - self.image.get_width(), self.rect.x)

    def moverIzquierda(self):
        self.rect.x -= 2
        limite = 0
        self.rect.x = max(self.rect.x, limite)

    def moverArriba(self):
        self.rect.y -= 2
        limite = 0
        self.rect.x = max(self.rect.y, limite)

    def moverAbajo(self):
        self.rect.y += 2
        limite = 0
        self.rect.x = max(self.rect.y, limite)

    def disparar(self, grupo_sprites_todos, grupo_sprites_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual > self.ultimoDisparo + 200:
            bala = Bala((self.rect.x + self.image.get_width() / 2, self.rect.y))
            grupo_sprites_todos.add(bala)
            grupo_sprites_balas.add(bala)
            self.ultimoDisparo = momento_actual
    #def draw()
    #   pass

class Enemigo(pygame.sprite.Sprite):
    #constructor
    def __init__(self, posicion):
        super().__init__()

        imagen = pygame.image.load("ufo1.png")
        self.image = pygame.transform.rotate(imagen, 180)
        self.image = pygame.transform.scale(self.image, (60, 60))
        #creamos el rect
        self.rect = self.image.get_rect()
        #actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.topleft = posicion
    def update(self, *args: any, **kwargs: any):
        self.rect.y += 1
        #capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if (self.rect.y > pantalla.get_height()):
            self.kill()
         #capturamos el args[2]
        grupo_sprites_balas = args[2]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprites_balas, pygame.sprite.collide_mask)
        if bala_colision:
            self.kill()
            bala_colision.kill()
class Fondo(pygame.sprite.Sprite):
    def __init__(self, posicion)-> None:
        super().__init__()
        pantalla = pygame.display.get_surface()
        imagen = pygame.image.load("space.jpg")
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), pantalla.get_height()))
        #creamos el rect
        self.rect = self.image.get_rect()
        #actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.topleft = (0,0)
class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.mask = pygame.mask.from_surface(self.image)
        self.image = pygame.transform.scale(self.image, (60, 60))
        #self.image = pygame.Surface((5,10))
        #self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y -= 5