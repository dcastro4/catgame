
from funciones.funciones import *
from funciones.graficar import *
from funciones.clases import *

   
def inicio(pantalla):
   
   
#if __name__=='__main__':
 
    dir=0
    sel=pygame.sprite.Group()
    s1=Seleccionar((350,200))
    sel.add(s1)
    var=100           
    image = pygame.image.load('graficos/Beauty Potion V2.png') 
    reloj=pygame.time.Clock()
    fin=False
    while not fin and var==100:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
        
                if event.key == pygame.K_UP:
                    dir=3
                    s1.update(dir, [0,60], [1,3]) 
                if event.key == pygame.K_DOWN:
                    dir=4
                    s1.update(dir, [0,60], [1,3]) 
                
                if event.key == pygame.K_RETURN:
                    if s1.lug[1]==1:
                        var=2
                    if s1.lug[1]==2:
                        var=4
                    if s1.lug[1]==3:
                        var=0
               
        
        image=pygame.transform.scale(image, (960, 512))
              
        pantalla.fill(NEGRO)
        pantalla.blit(image, (0,0))
        mostrarimg('graficos/sel.png', [0,190, 64, 70], (400, 250), [280,150], pantalla)  
        fuente= pygame.font.Font(None,28)
        texto= fuente.render("Selecciona la opción y oprime enter", 0, BLANCO)
        pantalla.blit(texto, (330,400))
        fuente= pygame.font.Font(None,50)
        texto= fuente.render("Catmonster odyssey", 0, (57, 255, 20))
        pantalla.blit(texto, (300,50))
        sel.draw(pantalla)
        pygame.display.flip()
        reloj.tick(30)

    if var==100:
        var=0
    return var
        