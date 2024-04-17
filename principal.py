import pygame
import json
from juego import *
from diseno import *
from inicio import *
from fin import *
from opciones import *
pantalla=pygame.display.set_mode([960, 512])
var=1
if __name__=='__main__':
    vol=1.0
    pygame.init()
    pygame.mixer.music.load('sonidos/Mutations.mp3')
    pygame.mixer.music.play(1)
    while(var!=0):
        
        if var==1:
            res=inicio(pantalla)
            var=res  
        if var==2:
            res=personalizar(pantalla)
            var=res    
        if var==3:
            res=jugar(pantalla)
            var=res  
        if var==4:
            res= opc(pantalla, vol)
            var=res[0]
            vol=res[1]
        if var==-1:
            res=fin(pantalla, vol)
            var=res  
        
    pygame.quit()