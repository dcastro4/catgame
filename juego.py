
from funciones.funciones import *
from funciones.graficar import *
from funciones.clases import *

def jugar(pantalla):              
        var=0      
    #if __name__=='__main__':
        pygame.init()
        gs=pygame.sprite.Group()
        rivales=pygame.sprite.Group()
        rivales_gen=pygame.sprite.Group()
        rivales2=pygame.sprite.Group()
        entities=pygame.sprite.Group()
        disp=pygame.sprite.Group()
        balas_enemigos = pygame.sprite.Group()
        posi=pygame.sprite.Group()
        bloques = pygame.sprite.Group()
        generadores = pygame.sprite.Group()
        enemy_generados = pygame.sprite.Group()

        # FONDO
        fondo = pygame.image.load("mapa/fondo.png")
        fondo = pygame.transform.scale2x(fondo) # 32 px --> 64 px
        info_img = fondo.get_rect()
        bg_width = info_img[2]
        bg_height = info_img[3]
        
        

        # LIMITES DE LA PANTALLA (PARA MOVER AL JUGADOR)
        lim_mov_der = (5/8)*ANCHO
        lim_mov_izq = (3/8)*ANCHO
        lim_mov_arr = (3/8)*ALTO
        lim_mov_aba = (5/8)*ALTO

        lim_windw_xmax = ANCHO - bg_width
        lim_windw_xmin = 0
        lim_windw_ymax = ALTO - bg_height
        lim_windw_ymin = 0

        # POSICION Y VELOCIDAD DE MOVIMIENTO DEL FONDO
        bg_posx = 0
        bg_velx = -5
        bg_posy = 0
        bg_vely = -5

        # LEER JSON
        nom_archivo = "mapa/mapa.json"
        with open(nom_archivo) as archivo:
            datos = json.load(archivo)
        capas = datos["layers"]

        plantas = capas[3]["data"]
        limite = capas[3]["width"]

        pos_x = 0
        pos_y = 0
        archivo_muros = "mapa/serenavillage/TX Tileset Wall.png"
        archivo_obsta = "mapa/serenavillage/TX Props.png"
        archivo_plants = "mapa/serenavillage/TX Plant.png"
        imgs_muros = recorte(archivo_muros, (16, 16))
        imgs_obsta = recorte(archivo_obsta, (16, 16))
        imgs_plants = recorte(archivo_plants, (16, 16))
        for obj in plantas:
            if obj > 320 and obj <= 576:
                obj = obj - 320

                i = obj//16
                j = obj%16 - 1
                img = imgs_plants[i][j]
                
                bloq = Bloque((64,64), (pos_x*64, pos_y*64), img)
                bloques.add(bloq)
            pos_x += 1
            if pos_x >= limite:
                pos_x = 0
                pos_y += 1
        muros = capas[2]["data"]
        limite = capas[2]["width"]

        pos_x = 0
        pos_y = 0
        for obj in muros:
            if obj != 0 and obj <= 320:
                obj = obj - 64

                i = obj//16
                j = obj%16 - 1
                img = imgs_muros[i][j]
                
                bloq = Bloque((64,64), (pos_x*64, pos_y*64), img)
                bloques.add(bloq)
            if obj != 0 and obj > 576 and obj <= 832:
                obj = obj - 576

                i = obj//16
                j = obj%16 - 1
                img = imgs_obsta[i][j]
                
                bloq = Bloque((64,64), (pos_x*64, pos_y*64), img)
                bloques.add(bloq)
            pos_x += 1
            if pos_x >= limite:
                pos_x = 0
                pos_y += 1
        
        dir=0
        r1=Rival((300,300), "graficos/enemigos/Soldier 03-4.png")
        rivales.add(r1)
        entities.add(r1)

        r2=Rival2((400,1100), "graficos/enemigos/Enemy 12-1.png")
        rivales2.add(r2)
        entities.add(r2)

        g1=Jugador((ANCHO/2, ALTO/3))
        gs.add(g1)
        p1=Posion((400, 200))
        posi.add(p1)

        img_gen = imgs_obsta[8][10] # IMAGEN DE LOS GENERADORES
        gen1 = Generador((64, 1024), img_gen)
        generadores.add(gen1)
        entities.add(gen1)

        gen2 = Generador((1024, 1088), img_gen)
        generadores.add(gen2)
        entities.add(gen2)

        gen3 = Generador((1088, 704), img_gen)
        generadores.add(gen3)
        entities.add(gen3)

        gen4 = Generador((2368, 320), img_gen)
        generadores.add(gen4)
        entities.add(gen4)

        reloj=pygame.time.Clock()
        fin=False

        # GENERAR LA COMIDA
        for i in range(30):
            p1=Posion((random.randrange(2880), random.randrange(1536)))
            posi.add(p1)

        destino_rivals = list() # LISTA PARA SACAR LOS RIVALES DE LOS GENERADORES

        while not fin and var==0:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    fin=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dir=1                          
                    if event.key == pygame.K_RIGHT:
                        dir=2
                    if event.key == pygame.K_UP:
                        dir=3
                    if event.key == pygame.K_DOWN:
                        dir=4   
                    if event.key ==pygame.K_SPACE:
                        pos=[g1.rect.x, g1.rect.y+20]
                        bala=Bala(pos, g1.dir)
                        disp.add(bala)

                if event.type == pygame.KEYUP:
                    dir=0
            
            # CONDICIONES DE FIN DE JUEGO
            if g1.vida<=0:
                var=-1
            if g1.rect.y > ALTO:
                var=-1


            # GENERACION DE RIVALES
            k = 0
            for generador in generadores:
                if generador.temp < 0:
                    k += 1
                    if k == 1:
                        spawn_point = (448, 416)
                    elif k == 2:
                        spawn_point = (1050, 1150)
                    elif k == 3:
                        spawn_point = (1100, 704)
                    elif k == 4:
                        spawn_point = (2400, 320)
                    else:
                        spawn_point = generador.rect.center
                    if random.randrange(10) >= 5:
                        enemy = Rival(spawn_point, "graficos/enemigos/Soldier 03-4.png")
                        rivales.add(enemy)
                    else:
                        enemy = Rival2(spawn_point, "graficos/enemigos/Enemy 12-1.png")
                        rivales2.add(enemy)
                    enemy_generados.add(enemy)
                    entities.add(enemy)
                    generador.entities += 1

                    generador.temp = random.randrange(400, 700)

            x = random.randrange(ANCHO)
            y = random.randrange(ALTO)
            destino_rivals.append((x,y))

            """i = 0
            for enemy in enemy_generados:
                if not in_range_entity(g1, enemy, 400, 0):
                    enemy.go_to(destino_rivals[i])
                i += 1"""

            # SI EL JUGADOR COME
            for bloq in bloques:           
                ls_col_posion = pygame.sprite.spritecollide(bloq, posi, True)
                for p in posi:           
                    if len(ls_col_posion)==0:
                        if colision(dir, g1, p):
                            if g1.vida<100:
                                g1.vida+=10
                                posi.remove(p)
            """for plant in plantas:           
                ls_col_posion = pygame.sprite.spritecollide(plant, posi, True)
                for p in posi:           
                    if len(ls_col_posion)==0:
                        if colision(dir, g1, p):
                            if g1.vida<100:
                                g1.vida+=10
                                posi.remove(p)"""

            # VALIDA SI LAS ENTIDADES ENEMIGAS COLISIONAN
            for riv in rivales:
                ls_col_ene = pygame.sprite.spritecollide(riv, bloques, False)

                if len(ls_col_ene):
                    riv.collide = True
                else:
                    riv.collide = False

            for riv in rivales2:
                ls_col_ene = pygame.sprite.spritecollide(riv, bloques, False)
                if len(ls_col_ene):
                    riv.collide = True
                else:
                    riv.collide = False
            """for riv in rivales2:
                ls_col_ene = pygame.sprite.spritecollide(riv, bloques, False)

                if len(ls_col_ene):
                    riv.collide = True
                else:
                    riv.collide = False"""
            
            # VALIDACION RANGO RIVALES
            for riv in rivales:
                if in_range_entity(g1, riv, 200, 10):
                    if not riv.collide:
                        riv.move = True
                        riv.go_to(g1.rect.center, True)
                    else:
                        riv.move = False
                else:
                    riv.move = False
            for riv in rivales2:
                if in_range_entity(g1, riv, 400, 250):
                    if not riv.collide:
                        riv.move = True
                        riv.go_to(g1.rect.center, True)
                    else:
                        riv.move = False
                elif in_range_entity(g1, riv, 250, 0):
                    if riv.timer_disp > 50:
                        pos_i = riv.rect.center
                        pos_f = g1.rect.center
                        bala_ene = Bala2(pos_i, pos_f)
                        if pos_i[0] < pos_f[0]:
                            bala_ene.velx = 10
                        else:
                            bala_ene.velx = -10
                        balas_enemigos.add(bala_ene)
                        riv.timer_disp = 0
                    else:
                        riv.timer_disp += 1
                else:
                    riv.move = False

            # GENERACION DE RIVALES
            """for generador in generadores:
                if generador.temp < 0:
                    enemy = Rival(generador.rect.center, "graficos/Soldier 03-4.png")
                    enemy_soldiers_gen.add(enemy)
                    enemy_soldiers.add(enemy)
                    x = random.randrange(ANCHO)
                    y = random.randrange(ALTO)
                    print(x, y)

                    generador.temp = random.randrange(100, 200)"""

            # SI COLISIONA CON UN ENEMIGO
            if dir!=0:
                for riv in rivales:
                    g1.vel=[5,5,5,5]
                    if (colision(dir, g1, riv)):
                        g1.vel[dir-1]=-25
                        g1.vida-=5                               
                ls_col2 = pygame.sprite.spritecollide(g1, bloques, False)
                for bloq in bloques:
                    if (colision(dir, g1, bloq)):
                        g1.vel[dir-1]=0
                gs.update(dir)

            # SI COLISIONA JUGADOR CON BALAS ENEMIGAS
            for b in balas_enemigos:
                if b.rect.x > ANCHO or  b.rect.x < 0 or b.rect.y > ALTO or b.rect.y < 0:
                    balas_enemigos.remove(b)
                ls_col_b_play = pygame.sprite.spritecollide(g1, balas_enemigos, True)
                if len(ls_col_b_play) > 0:
                    g1.vida -= 5

            for b in disp:
                if b.rect.x > ANCHO or  b.rect.x < 0 or b.rect.y > ALTO or b.rect.y < 0:
                    disp.remove(b)
                # COLISION BALA CON BLOQUES
                ls_col3 = pygame.sprite.spritecollide(b, bloques, False)
                ls_col_gen_disp = pygame.sprite.spritecollide(b, generadores, False)
                for bloq in bloques:
                    if colision(b.dir, b, bloq):
                        disp.remove(b)
                for gen in ls_col_gen_disp:
                    gen.vida -= 10
                    if gen.vida == 10:
                        generadores.remove(gen)
                        entities.remove(gen)

                for r in rivales:
                    if pygame.sprite.collide_rect(b, r):
                        disp.remove(b)
                        r.vida-=30
                    if r.vida<=0:
                        rivales.remove(r)
                        entities.remove(r)
                for r in rivales2:
                    if pygame.sprite.collide_rect(b, r):
                        disp.remove(b)
                        r.vida-=30
                    if r.vida<=0:
                        rivales2.remove(r)
                        entities.remove(r)
                for r in enemy_generados:
                    if pygame.sprite.collide_rect(b, r):
                        disp.remove(b)
                        r.vida-=30
                    if r.vida<=0:
                        enemy_generados.remove(r)
                        entities.remove(r)

            for p in posi:
                if colision(dir, g1, p):
                    if g1.vida<100:
                        g1.vida+=10
                        posi.remove(p)

            # CONDICIONES PARA EL MOVIMIENTO DEL FONDO
            if g1.rect.right > lim_mov_der and bg_posx > lim_windw_xmax:
                g1.rect.right = lim_mov_der
                bg_posx += bg_velx
                for b in bloques:
                    b.rect.x += bg_velx
                for riv in entities:
                    riv.rect.x += bg_velx
                for pot in posi:
                    pot.rect.x += bg_velx

            if g1.rect.left < lim_mov_izq and bg_posx < lim_windw_xmin:
                g1.rect.left = lim_mov_izq
                bg_posx -= bg_velx
                for b in bloques:
                    b.rect.x -= bg_velx
                for riv in entities:
                    riv.rect.x -= bg_velx
                for pot in posi:
                    pot.rect.x -= bg_velx

            if g1.rect.top < lim_mov_arr and bg_posy < lim_windw_ymin:
                g1.rect.top = lim_mov_arr
                bg_posy -= bg_vely
                for b in bloques:
                    b.rect.y -= bg_vely
                for riv in entities:
                    riv.rect.y -= bg_vely
                for pot in posi:
                    pot.rect.y -= bg_vely

            if g1.rect.bottom > lim_mov_aba and bg_posy > lim_windw_ymax:
                g1.rect.bottom = lim_mov_aba
                bg_posy += bg_vely
                for b in bloques:
                    b.rect.y += bg_vely
                for riv in entities:
                    riv.rect.y += bg_vely
                for pot in posi:
                    pot.rect.y += bg_vely
                    
                    
       

            disp.update()
            generadores.update()
            rivales.update()
            rivales2.update()
            enemy_generados.update()
            balas_enemigos.update()
        
            pantalla.fill(NEGRO)
            pantalla.blit(fondo, (bg_posx,bg_posy))

            posi.draw(pantalla)
            disp.draw(pantalla)
            
            bloques.draw(pantalla)
            generadores.draw(pantalla)
            balas_enemigos.draw(pantalla)
            gs.draw(pantalla)
            rivales.draw(pantalla)
            rivales2.draw(pantalla)
            enemy_generados.draw(pantalla)

            vida(pantalla,[10,10], 2, g1.vida)       
            # vida(pantalla,[r1.rect.left-10, r1.rect.top-30], 1, r1.vida)
            for ent in entities:
                vida(pantalla,[ent.rect.left-10, ent.rect.top-30], 1, ent.vida)
            pygame.display.flip()
            reloj.tick(30)    
    
        return var      