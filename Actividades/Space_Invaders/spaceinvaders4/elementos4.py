import pygame

class Nave(pygame.sprite.Sprite):
    # Aqui creamos el costructor
    def __init__(self, posicion) -> None:
        super().__init__()
        # Cargamos la imagen
        images = [pygame.image.load("avion.png"),pygame.image.load("avion2.png")]
        self.images = [pygame.transform.scale(images[0],(30,60)),pygame.transform.scale(images[1],(30,60))]
        self.indice_images = 0
        self.image = self.images[self.indice_images]
        self.contador_image = 0
        # Creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo
        self.rect.topleft=posicion
        self.ultimo_disparo = 0
        
    # Update
    def update (self,*args: any,**kwargs: any):
        # Capturamos las teclas
        teclas = args[0]
        # Capturamos grupo_sprite_todos
        grupo_sprite_todos = args[1]
        # Capturamos grupo_sprite_balas
        grupo_sprite_balas = args[2]
        # Capturamos la pantalla
        pantalla = pygame.display.get_surface()
        # Gestionamos las teclas
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
        # Aqui disparamos.
        if teclas[pygame.K_SPACE]:
            self.disparar(grupo_sprite_todos, grupo_sprite_balas)
        
        if teclas[pygame.K_RIGHT]:
            self.rect.x +=2
            pantalla = pygame.display.get_surface()
            self.rect.x = min(pantalla.get_width()-self.image.get_width(), self.rect.x)
        # Gestionamos la animacion
        self.contador_image = (self.contador_image + 1) % 40
        self.indice_images = self.contador_image // 20
        self.image = self.images[self.indice_images]
    
    def disparar(self, grupo_sprite_todos, grupo_sprite_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual >  self.ultimo_disparo +200:
            bala = Bala((self.rect.x + self.image.get_width() /2, self.rect.y))
            grupo_sprite_todos.add(bala)
            grupo_sprite_balas.add(bala)
            self.ultimo_disparo = momento_actual
        
class Enemigo(pygame.sprite.Sprite):
    # Aqui creamos el costructor
    def __init__(self, posicion) -> None:
        super().__init__()
        # Cargamos la imagen
        imagen = pygame.image.load("ufo1.png")
        self.image = pygame.transform.scale(imagen,(60,30))
        self.image = pygame.transform.rotate(self.image, 180)
        self.mask = pygame.mask.from_surface(self.image)
        # Creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo
        self.rect.topleft = posicion
        
    def update (self,*args: any,**kwargs: any) -> None:
        self.rect.y += 1
        # Capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if (self.rect.y > pantalla.get_height()):
            self.kill()
            
        #Capturamos el argumento 2 -> grupo_sprite_balas
        grupo_sprite_balas = args[2]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprite_balas, pygame.sprite.collide_mask)
        if bala_colision:
            self.kill()
            bala_colision.kill()
            
class Fondo(pygame.sprite.Sprite):
    def _init_(self, posicion) -> None:
        super().__init__()
        images = pygame.image.load("space.jpg")
        pantalla = pygame.display.get_surface()
        self.image = pygame.transform.scale(images, (pantalla.get_width(), images.get_height()))
        # Creamos el rect
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo
        self.rect.topleft = posicion
        
class Bala(pygame.sprite.Sprite):
    def _init_(self, posicion) -> None:
        super().__init__()
        image = pygame.image.load("laser.png")
        self.image = pygame.transform.scale(image,(30,30))
        #Creamos un rectangulo
        #self.image = pygame.Surface((5,10))
        #self.image.fill((255,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion
        
    def update (self,*args: any,**kwargs: any) -> None:
        self.rect.y -=5