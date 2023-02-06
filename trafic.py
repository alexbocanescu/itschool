import pygame
from pygame.locals import *
import random


alb = (255, 255, 255)
gri = (50, 50, 50)
verde = (0, 255, 0)
rosu = (255, 0, 0)
latime = 600
inaltime = 600
latime_strada = int(latime/1.6)
latime_linie = int(latime/80)
banda_dreapta = latime/2 + latime_strada/4
banda_stanga = latime/2 - latime_strada/4


pygame.init()
running = True
ecran = pygame.display.set_mode((latime, inaltime))
pygame.display.set_caption('Trafic pe E85')
ecran.fill(verde)

pygame.display.update()

masina = pygame.image.load('purplecar.jpg')
loc_masina = masina.get_rect()
loc_masina.center = banda_dreapta, inaltime*0.8

masina2 = pygame.image.load('redcar.jpg')
loc_masina2 = masina2.get_rect()
loc_masina2.center = banda_stanga, inaltime*0.2


while running:
    loc_masina2[1] += 1
    if loc_masina2[1] > latime:
        if random.randint(0, 1) == 0:
            loc_masina2.center = banda_dreapta, -300
        else:
            loc_masina2.center = banda_stanga, -300
    if loc_masina[0] == loc_masina2[0] and loc_masina2[1] > loc_masina[1]:
        ecran.fill(rosu)
        pygame.display.update()
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                loc_masina = loc_masina.move([-int(latime_strada/2), 0])
            if event.key == K_RIGHT:
                loc_masina = loc_masina.move([int(latime_strada/2), 0])

    pygame.draw.rect(ecran, gri, (latime / 2 - latime_strada / 2, 0, latime_strada, inaltime))
    pygame.draw.rect(ecran, alb, (latime / 2 - latime_linie / 2, 0, latime_linie, latime))
    pygame.draw.rect(ecran, alb, (latime / 2 - latime_strada / 2 + latime_linie * 2, 0, latime_linie, latime))
    pygame.draw.rect(ecran, alb, (latime / 2 + latime_strada / 2 - latime_linie * 3, 0, latime_linie, latime))

    ecran.blit(masina, loc_masina)
    ecran.blit(masina2, loc_masina2)
    pygame.display.update()

pygame.quit()
