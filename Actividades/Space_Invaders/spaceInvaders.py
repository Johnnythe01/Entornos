import pygame
from Elementos import Nave, Fondo

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
reloj = pygame.time.Clock()
FPS = 60

salir = False

nave = Nave()

fondo = Fondo()
while not salir:
    reloj.tick(60)
    # gestionar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir = True

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        nave.moverIzquierda()
    if teclas[pygame.K_RIGHT]:
        nave.moverDerecha()
    if teclas[pygame.K_UP]:
        nave.moverArriba()
    if teclas[pygame.K_DOWN]:
        nave.moverAbajo()

    #gestionar cambios
    #pantalla.fill((0, 15, 80))
    fondo.dibujar()
    # pygame.draw.rect(pantalla, (255,255,255), pygame.Rect(posIzda,posTop,60,60))
    nave.dibujar()
    # redibujar el juego
    pygame.display.flip()

pygame.quit()