import pygame

class Nave:
    def __init__(self) -> None:
        self.x = 30
        self.y = 30
        imagenes_cargadas = [pygame.image.load("Actividades/Space_Invaders/avion.png"), pygame.image.load("Actividades/Space_Invaders/avion2.png")]
        self.imagenes = [pygame.transform.scale(imagenes_cargadas[0], (60,60)), pygame.transform.scale(imagenes_cargadas[1], (60,60))]
        self.contador = 0

    def moverDerecha(self):
        self.x += 10
        pantalla = pygame.display.get_surface()
        limite = pantalla.get_width()
        self.x = min(self.x, limite - self.imagenes[0].get_width())

    def moverIzquierda(self):
        self.x -= 10
        pantalla = pygame.display.get_surface()
        limite = 0
        self.x = max(self.x, limite)

    def moverAbajo(self):
        self.y += 10

    def moverArriba(self):
        self.y -= 10

    def dibujar(self):
        #aumento el contador
        self.contador = (self.contador + 1) % 40
        #cojo el puntero a la pantalla
        pantalla = pygame.display.get_surface()
        #seleccionar la imagen que toca
        seleccionada = self.contador // 20
        #dibujar imagen
        pantalla.blit(self.imagenes[seleccionada], (self.x, self.y))