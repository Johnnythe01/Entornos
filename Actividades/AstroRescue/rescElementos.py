import pygame

class Nave(pygame.sprite.Sprite):
    # Constructor
    def __init__(self, posicion):
        super().__init__()
        # Cargamos la imagen
        self.imagennave = pygame.transform.scale(pygame.image.load("ambulancia.png"), (50, 50))
        self.imagennave2 = pygame.transform.scale(pygame.image.load("ambulanciaizq.png"), (50, 50))
        self.image = self.imagennave
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
        # capturamos enemigo colision with my self 
        grupo_sprite_enemigos = args[3]
        # Capturamos la pantalla
        pantalla = pygame.display.get_surface()
        # Gestionamos las teclas
        if teclas[pygame.K_LEFT]:
            self.rect.x -= 4
            self.rect.x = max(0, self.rect.x)
            self.image = self.imagennave2  # Use the left-facing image
        elif teclas[pygame.K_RIGHT]:
            self.rect.x += 4
            self.rect.x = min(pantalla.get_width() - self.image.get_width(), self.rect.x)
            self.image = self.imagennave  # Use the right-facing image

        if teclas[pygame.K_SPACE]:
            self.disparar(grupo_sprites_todos, grupo_sprites_balas)

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
        imagen = pygame.image.load("bombacolor.png")
        self.image = pygame.transform.scale(imagen, (50,50))
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
        
        grupo_sprite_enemigos = args[3]
        enemigo_colision = pygame.sprite.spritecollideany(self, grupo_sprite_enemigos, pygame.sprite.collide_mask)
        if enemigo_colision:
            self.kill()
            enemigo_colision.kill()
            print("Vida del enemigo:", self.vida)
            if self.vida <= 0:
                self.kill()  # Eliminamos el enemigo si su vida llega a
                
class Fondo(pygame.sprite.Sprite):
    def __init__(self, posicion)-> None:
        super().__init__()
        pantalla = pygame.display.get_surface()
        imagen = pygame.image.load("battleground.jpg")
        self.image = pygame.transform.scale(imagen, (pantalla.get_width(), pantalla.get_height()))
        # Creamos el rect
        self.rect = self.image.get_rect()
        # Actualizamos la posicion del rectangulo para que coincida con la posicion
        self.rect.topleft = (0,0)

class Bala(pygame.sprite.Sprite):
    def __init__(self, posicion) -> None:
        super().__init__()
        self.image = pygame.image.load("cruzroja.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        # Creamos un rectangulo
        #self.image = pygame.Surface((5,10))
        #self.image.fill((255,0,0))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = posicion

    def update(self, *args: any, **kwargs: any) -> None:
        self.rect.y -= 5