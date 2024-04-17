
from funciones.funciones import *
from funciones.graficar import *
from funciones.clases import *

   
def fin(pantalla, vol):
   
   
#if __name__=='__main__':
 
    pygame.init()
    var=0        
    pygame.mixer.init()
    pygame.mixer.music.load('sonidos/fin.mp3')
    image = pygame.image.load('graficos/New Letter.png') 
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(vol)
    
    reloj=pygame.time.Clock()
    fin=False
    while not fin and var==0:
       
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:               
                if event.key == pygame.K_RETURN:
                    var=1
                
        image=pygame.transform.scale(image, (960, 512))
              
        pantalla.fill(NEGRO)
        pantalla.blit(image, (0,0))  
        
        
        fuente= pygame.font.Font(None,28)
        texto= fuente.render("Oprime enter para volver a inicio", 0, BLANCO)
        pantalla.blit(texto, (320,400))
        
        fuente= pygame.font.Font(None,60)
        texto= fuente.render("Fin de juego", 0, (255, 160, 122))
        pantalla.blit(texto, (350,300))   
        
        
        pygame.display.flip()
        reloj.tick(30)     
  
    return var
