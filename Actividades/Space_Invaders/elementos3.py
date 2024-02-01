import pygame

class Nave(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, posicion):
        super().__init__()
        # Cargamos la imagen
        imagen = [pygame.image.load("avion.png"), pygame.image.load("avion2.png"), ]
        self.imagennave = [pygame.transform.scale(imagen[0], (50, 50)), pygame.transform.scale(imagen[1], (50, 50))]
        self.indicenave = 0
        self.image = self.imagennave[self.indicenave]
        self.contador_imagen = 0
        # Creamos un rectangulo a partir de la iamgen
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.center = posicion
        self.ultimoDisparo = 0
    
    # Update
    def update(self, *args: any, **kwargs: any):
        # Capturamos las teclas.
        teclas = args[0]
        # Capturamos grupo sprites todos.
        grupo_sprites_todos = args[1]
        # Capturamos grupo sprites balas.
        grupo_sprites_balas = args[2]
        # Capturamos la pantalla
        pantalla = pygame.display.get_surface()
        # Gestionamos las teclas
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 2
            self.rect.x = max(0, self.rect.x)
            # Disparar
        if teclas[pygame.K_SPACE]:
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)

        if teclas[pygame.K_RIGHT]:
            self.rect.x +=2
            pantalla = pygame.display.get_surface()
            self.rect.x = min(pantalla.get_width()-self.image.get_width(), self.rect.x)
        
        if teclas[pygame.K_UP]:
            self.rect.y -= 2
            self.rect.y = max(0, self.rect.y)

        if teclas[pygame.K_DOWN]:
            self.rect.y +=2
            pantalla = pygame.display.get_surface()
            self.rect.y = min(pantalla.get_height()-self.image.get_height(), self.rect.y)
        
        # Gestionamos la animación
        self.contador_imagen = (self.contador_imagen + 1) % 40
        self.indicenave = self.contador_imagen // 20
        self.image = self.imagennave[self.indicenave]

    def disparar(self, grupo_sprite_todos, grupo_sprite_balas):
        momento_actual = pygame.time.get_ticks()
        if momento_actual >  self.ultimoDisparo +200:
            bala = Bala((self.rect.x + self.image.get_width() /2, self.rect.y))
            grupo_sprite_todos.add(bala)
            grupo_sprite_balas.add(bala)
            self.ultimoDisparo = momento_actual

class Enemigo(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, posicion):
        super().__init__()
        # Cargamos la imagen
        imagen = pygame.image.load("ufo1.png")
        self.image = pygame.transform.scale(imagen, (50,50))
        self.image = pygame.transform.rotate(self.image, 180)
        self.mask = pygame.mask.from_surface(self.image)
        # Creamos un rectangulo a partir de la imagen
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.topleft = posicion
        self.vida = 1  # Inicializamos la vida del enemigo

    def update(self, *args: any, **kwargs: any):
        self.rect.y += 1
        # Capturamos la pantalla
        pantalla = pygame.display.get_surface()
        if (self.rect.y > pantalla.get_height()):
            self.kill()

        # Creamos la colision
            self.vida -= 1
            print(self.vida)
            if self.vida == 0:
                self.kill()

        # Capturamos el args[2] (Argumento 2) -> grupo_sprite_balas
        grupo_sprites_balas = args[2]
        bala_colision = pygame.sprite.spritecollideany(self, grupo_sprites_balas, pygame.sprite.collide_mask)
        if bala_colision:
            self.kill()
            bala_colision.kill()
            print("Vida del enemigo:", self.vida)
            if self.vida <= 0:
                self.kill()  # Eliminamos el enemigo si su vida llega a 0

class Fondo(pygame.sprite.Sprite):
    def __init__(self, posicion)-> None:
        super().__init__()
        pantalla = pygame.display.get_surface()
        imagen = pygame.image.load("space.jpg")
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), pantalla.get_height()))
        # Creamos el rect
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.topleft = (0,0)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("laser.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        # Creamos un rectangulo
        #self.image = pygame.Surface((5,10))
        #self.image.fill((255,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y -= 5
