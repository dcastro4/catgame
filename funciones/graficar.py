import pygame
import math

BLANCO=(255,255,255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL=(0, 47, 187)
VERDE=[0,255,0]
PURPURA_S=[255,204,255]
GRIS=[200,200,200]
#inicio 

#personalizacion de personaje---------------------------------------------------------

def mostrarimg(dir, recorte, escala, pos, pantalla):
    sheet = (pygame.image.load(dir))
    sheet.set_clip(pygame.Rect(recorte))
    image =sheet.subsurface(sheet.get_clip())
    image=pygame.transform.scale(image, escala)
    pantalla.blit(image, pos)

def cargarImages(pantalla):
    mostrarimg('graficos/sel.png', [80,95, 32, 32], (300, 250), [580,100], pantalla)
    mostrarimg('graficos/neko3.png', [32,0, 2*16, 2*16], (200, 200), [620,130], pantalla)
    
def dibujar(pantalla):
    elec=["COLOR", "OJOS", "ROPA", "SOMBREROS"]
    
    for i in range(0,4):
        mostrarimg('graficos/sel.png', [143,80, 50,15], (400, 80), [130, 55+i*100],pantalla)
        
        fuente= pygame.font.Font(None,30)
        texto= fuente.render( elec[i], 0, (37, 40, 80))
        pantalla.blit(texto, (160,70+i*100))
        
        for e in range(1,8): 
            fuente= pygame.font.Font(None,40)
            texto= fuente.render(str(e) , 0, BLANCO)
            pantalla.blit(texto, (130+e*50,100+i*100))


#juego principal-----------------------------------------------

def vida(pantalla,posicion, escala, vida):
    if vida>0:
        image = pygame.image.load('graficos/HP_bar_1.png')     
        image=pygame.transform.scale(image, (80*escala, 16*escala))
        pantalla.blit(image, posicion)
        vid=(60*escala*vida)/100
        pygame.draw.rect(pantalla,  ROJO, [(posicion[0]+17*escala)+math.ceil(escala*0.5), posicion[1]+3*escala, vid, 10*escala], 0)