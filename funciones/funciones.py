import pygame
import math
import numpy as np
import random
import json
from PIL import Image

BLANCO=(255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL=(0, 47, 187)
VERDE=[0,255,0]
PURPURA_S=[255,204,255]
GRIS=[200,200,200]
ANCHO=960
ALTO=512
px=32
CAFE=(205, 133, 63)

#personalizacion de personaje---------------------------------------------------------


def actualizar(num):   
    lista=["0skin", "1Eye", "2Costume","3Hat","4Tail"]

    for i in range(0,5):
        foreground = Image.open("graficos/personaje/"+lista[i]+"/"+str(num[i])+".png")
        if i == 0:
            background = Image.open('graficos/blanco.png')
        else:
            background = Image.open('graficos/neko3.png')
        background.paste(foreground, (0, 0), foreground.convert('RGBA'))
        background.save("graficos/neko3.png")   
        
#juego principal-----------------------------------------------

#calcula las posiciones del recorte segun cuantos animaciones tenga el sprite

def recortar(filas, columnas, inicio, tamaño):
    principal=[]
    for f in range (0, filas):
        lista = []
        inix=inicio[0]
        for c in range (0, columnas):
            lista.append([inix*px, inicio[1]*px, tamaño[0]*px, tamaño[1]*px])   
            inix+=tamaño[0]
                
        principal.append(lista)
        inicio[1]+=tamaño[1]
    return principal

def recorte(imagen, cant_sprts):

    img = pygame.image.load(imagen)

    size = img.get_rect()
    desp_x = size[2] / cant_sprts[0]
    desp_y = size[3] / cant_sprts[1]
    matrix_imgs = list()

    for i in range(cant_sprts[1]):
        ls_imgs_fla = list()
        for j in range(cant_sprts[0]):
            cuadro = img.subsurface(j * desp_x, i * desp_y, desp_x, desp_y)
            ls_imgs_fla.append(cuadro)
        matrix_imgs.append(ls_imgs_fla)

    return matrix_imgs

#colisiones segun dirección
def colision(direc, principal, colisionable):
    var=False
    medidas=[principal.rect.top, principal.rect.bottom, principal.rect.right, principal.rect.left]

    if direc==1:
    
        if colisionable.rect.collidepoint(medidas[3]+10, medidas[0]+50):
            var=True
                  
    if direc==2:

        if colisionable.rect.collidepoint(medidas[2]-10, medidas[0]+50):
            var=True                 
                     
    if direc==3:

        if colisionable.rect.collidepoint(medidas[2]-20, medidas[0]+40):
            var=True
        if colisionable.rect.collidepoint(medidas[3]+20, medidas[0]+40):
            var=True
                        
    if direc==4:
    
        if colisionable.rect.collidepoint(medidas[3]+20, medidas[1]):
            var=True
            
        if colisionable.rect.collidepoint(medidas[2]-20, medidas[1]):
            var=True   
    return var

def move_ent_y(ent, pos):
    x1 = pos[0]
    y1 = pos[1]

    x2 = ent.rect.center[0]
    y2 = ent.rect.center[1]
    
    if (y1 - y2) > 0 and abs(y1-y2) >= ent.rapidez:
        ent.rect.y += ent.rapidez
        ent.vely = 1
    if (y1 - y2) < 0 and abs(y1-y2) >= ent.rapidez:
        ent.rect.y -= ent.rapidez
        ent.vely = -1
    ent.velx = 0

def move_ent_x(ent, pos):
    x1 = pos[0]
    y1 = pos[1]

    x2 = ent.rect.center[0]
    y2 = ent.rect.center[1]

    if (x1 - x2) > 0 and abs(x1-x2) >= ent.rapidez:
        ent.rect.x += ent.rapidez
        ent.velx = 1
    if (x1 - x2) < 0 and abs(x1-x2) >= ent.rapidez:
        ent.rect.x -= ent.rapidez
        ent.velx = -1
    ent.vely = 0

def in_range_entity(ent1, ent2, d_ran, d_min):
    x1 = ent1.rect.center[0]
    y1 = ent1.rect.center[1]

    x2 = ent2.rect.center[0]
    y2 = ent2.rect.center[1]

    d_betw = ((y2-y1)**2 + (x2-x1)**2)**(1/2)

    if d_betw < d_ran and d_betw > d_min:
        return True
    else:
        return False