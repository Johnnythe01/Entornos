import pygame
import math

class Nave:
    def __init__(self) -> None:
        self.x = 400
        self.y = 500
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
        # cojo el puntero a la pantalla
        pantalla = pygame.display.get_surface()
        # seleccionar la imagen que toca
        seleccionada = self.contador // 20
        # dibujar imagen
        pantalla.blit(self.imagenes[seleccionada], (self.x, self.y))

class Fondo:
    def __init__(self) -> None:
        # localizar la pantalla
        pantalla = pygame.display.get_surface()
        # cargamos la imagen
        imagen = pygame.image.load("\Actividades\Space_Invaders\space.jpg")
        # escalar la imagen para que encaje en el ancho de la pantalla
        self.fondo = pygame.transform.scale(imagen, (pantalla.get_width(), imagen.get_height))
        # scroll
        self.scroll = 0
        # cuantas piezas de fondo necesitamos
        self.piezas = math.ceil(pantalla.get_height() / self.fondo.get_height()) +1

    def dibujar(self):
        # aumentar el scroll
        self.scroll += 10
        # localizar la pantalla
        pantalla = pygame.display.get_surface()
        # resetear el scroll
        if self.scroll > pantalla.get_height():
            self.scroll = 0
        # dibujamos el fondo
        for i in range(0, self.piezas):
            pantalla.blit(self.fondo, (0, - self.fondo.get_height() + i * self.fondo.get_height() + self.scroll))