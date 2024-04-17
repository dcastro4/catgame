
from funciones.funciones import *
from funciones.graficar import *
from funciones.clases import *

   
def opc(pantalla, vol):
    
   
#if __name__=='__main__':
  
    pygame.init()
    var=0        
    image = pygame.image.load('graficos/Spider Desktop.png') 
    reloj=pygame.time.Clock()
    fin=False
    
    lista=[["Oprime enter para volver a inicio", BLANCO, 28, (320,400)], 
            ["Musica", CAFE, 40, (400,150)],
            ["Opciones y creditos", (57, 255, 20), 60, (100,40)],
            [" mutaciones, https://www.fiftysounds.com/es/", BLANCO, 24, (400,180)],
            [" Persecution, Soykhaler:", BLANCO, 24, (400,200)],
            [" https://pixabay.com/es/music/suspenso-persecution-9790/", BLANCO, 24, (400,220)],
            ["Graficos", CAFE, 40, (400,250)],
            ["https://cainos.itch.io/,  https://albertmixalev.itch.io/", BLANCO, 27, (400,280)],
            ["https://mounirtohami.itch.io/, https://pipoya.itch.io/", BLANCO, 27, (400,300)],
            ["https://royal-naym.itch.io/, https://henrysoftware.itch.io/", BLANCO, 27, (400,320)],
            ["utiliza las flechas para aumentar o disminuir el sonido", BLANCO, 27, (120,120)],
             ["Creadores: Diego Alejandro Castro y Sofía Sierra Cardona", CAFE, 27, (100,470)]         
          ]
    

    while not fin and var==0:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:               
                if event.key == pygame.K_RETURN:
                    var=1
           
                if event.key == pygame.K_LEFT:
                    if vol>0.1:
                        vol-=0.1
                
                if event.key == pygame.K_RIGHT:
                    if vol<1.0:
                        vol+=0.1
                   

        image=pygame.transform.scale(image, (960, 512))
        pygame.mixer.music.set_volume(vol)
        pantalla.fill(NEGRO)
        pantalla.blit(image, (0,0))  
        mostrarimg('graficos/sel.png',[148, 35, 16, 10], (256, 160), (240,200), pantalla)
        mostrarimg('graficos/sel.png',[130, 35, 16, 10], (256, 160), (80,200), pantalla)
        for i in lista:
            fuente= pygame.font.Font(None,i[2])
            texto= fuente.render(i[0], 0, i[1])
            pantalla.blit(texto, i[3])
    
        
        fuente= pygame.font.Font(None,40)
        texto= fuente.render("Musica al "+str(math.floor(vol*100))+"%", 0, CAFE)
        pantalla.blit(texto, (150, 350))
        pygame.display.flip()
        reloj.tick(30)     
  
    return [var, vol]
