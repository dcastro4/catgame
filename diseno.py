
from funciones.funciones import *
from funciones.graficar import *
from funciones.clases import *


def personalizar(pantalla): 
    
    var=0      
#if __name__=='__main__':
    pygame.init()
    img=[1,1,1,1,1]
    actualizar(img)
    dir=0
    sel=pygame.sprite.Group()
    s1=Seleccionar((150,100))
    sel.add(s1)

    reloj=pygame.time.Clock()
    fin=False
    while not fin and var==0:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dir=1           
                    s1.update(dir, [50,100], [7,4])               
                if event.key == pygame.K_RIGHT:
                    dir=2
                    s1.update(dir, [50,100], [7,4])
                if event.key == pygame.K_UP:
                    dir=3
                    s1.update(dir, [50,100], [7,4])
                if event.key == pygame.K_DOWN:
                    dir=4
                    s1.update(dir, [50,100], [7,4])
              
               
                if event.key == pygame.K_SPACE:
                    #enter= K_RETURN
                    img[s1.lug[1]-1]=s1.lug[0]
                    img[4]=img[0]        
                    actualizar(img)
                    
                if event.key == pygame.K_RETURN:
                        var=3
                        
         
                    
        pantalla.fill(NEGRO)
        dibujar(pantalla)
        fuente= pygame.font.Font(None,25)
        texto= fuente.render("Para seleccionar espacio y para continuar enter", 0, BLANCO)
        pantalla.blit(texto, (550,400))
        sel.draw(pantalla)
        cargarImages(pantalla)
        pygame.display.flip()
        reloj.tick(30)
        
    return var
        