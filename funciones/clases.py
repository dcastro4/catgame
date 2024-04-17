from funciones.funciones import *


#personalizacion de personaje---------------------------------------------------------

class Seleccionar(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
     
        self.sheet = pygame.image.load('graficos/sel.png')
        self.sheet.set_clip(pygame.Rect([148, 35, 16, 10]))
        self.image= self.sheet.subsurface(self.sheet.get_clip())
        self.image=pygame.transform.scale(self.image, (px*2, 40))
        self.rect = self.image.get_rect()    
        self.rect.x=pos[0]
        self.rect.y=pos[1]   
        self.dir=0
        self.lug=[1,1]
  
    def update(self, direction, movim, lim):
        self.dir=direction     
        if direction == 1:
            if (self.lug[0]-1)>0:
                self.lug[0]-=1
                self.rect.x -= movim[0]
               
        if direction == 2:
            if self.lug[0]+1<(lim[0]+1):
                self.lug[0]+=1
                self.rect.x += movim[0]
                
        if direction == 3:       
            if self.lug[1]-1>0:
                self.lug[1]-=1
                self.rect.y -= movim[1]
           
                
        if direction == 4:
            if self.lug[1]+1<(lim[1]+1):
                self.lug[1]+=1        
                self.rect.y += movim[1]
           
    

#juego principal-----------------------------------------------


class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        
        pygame.sprite.Sprite.__init__(self)     
        imagen=recortar(4, 3, [0,0], [2,2]) 
        self.sheet = (pygame.transform.scale2x(pygame.image.load('graficos/neko3.png')))
        self.sheet.set_clip(pygame.Rect(imagen[0][0]))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]   
        self.vel=[5, 5, 5, 5] 
        self.dir=4
        self.frame=0.0
        self.vida=100
        self.left_states=imagen[1]
        self.right_states=imagen[2]
        self.up_states=imagen[3]
        self.down_states=imagen[0]
        
        
    def clip(self, clipped_rect):
        self.frame+=0.2
        if math.floor(self.frame)>2:
            self.frame=0 
        clipped_rect=clipped_rect[math.floor(self.frame)]  
        self.sheet.set_clip(pygame.Rect(clipped_rect))
       
        return clipped_rect

    def update(self, direction):
        self.dir=direction  
        if direction == 1:
            self.clip(self.left_states)
            self.rect.x -= self.vel[0] 
        if direction == 2:
            self.clip(self.right_states)
            self.rect.x += self.vel[1] 
        if direction == 3:
            self.clip(self.up_states)
            self.rect.y -= self.vel[2] 
        if direction == 4:
            self.clip(self.down_states)
            self.rect.y += self.vel[3] 
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
 #(pygame.transform.scale2x(pygame.image.load('graficos/poder.png')))   


class Bala(pygame.sprite.Sprite):
    def __init__(self, pos, num):
        pygame.sprite.Sprite.__init__(self)
        self.imagen=recortar(1, 8, [0,0], [2,2])
        self.im=self.imagen[0] 
        self.imagen=self.imagen[0][0]
        self.sheet = (pygame.transform.scale2x(pygame.image.load('graficos/poder.png')))
        self.sheet.set_clip(pygame.Rect(self.imagen))   
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        
        if num==1:        
            self.image = (pygame.transform.flip(self.image, True, False))    
        if num==3:      
            self.image = pygame.transform.rotate(self.image, 90)  
        if num==4:      
            self.image = pygame.transform.rotate(self.image, 270) 
        self.dir=num
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=20
        self.vely=20
        self.frame=0.0
        
    def update(self): 
        
        self.frame+=0.5
        if math.floor(self.frame)>7:
            self.frame=0 
        clipped_rect=self.im[math.floor(self.frame)]
        self.sheet.set_clip(pygame.Rect(clipped_rect))
        self.clip=clipped_rect
        self.image = self.sheet.subsurface(self.sheet.get_clip())
      
        if self.dir==1:
            self.image = (pygame.transform.flip(self.image, True, False))    
            self.rect.x -= self.velx
            if self.rect.x<0:
                self.velx=0      
        if self.dir==2:
            self.rect.x += self.velx
            if self.rect.x>ANCHO:
                self.velx=0
        if self.dir==3: 
            self.image = pygame.transform.rotate(self.image, 90)
            self.rect.y -= self.vely
            if self.rect.y<0:
                self.vely=0                 
        if self.dir==4: 
            self.image = pygame.transform.rotate(self.image, 270) 
            self.rect.y += self.vely
            if self.rect.y>ALTO:
                self.vely=0
      
                
class Rival(pygame.sprite.Sprite):
    def __init__(self, pos, dir_img):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = recorte(dir_img, (3, 4))
        self.fil = 0
        self.col = 1
        self.frame = 0.0
        self.image = pygame.transform.scale2x(self.imgs[self.fil][self.col])
        # self.image = self.imgs[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vida = 100
        self.vel = [0,0,0,0]
        self.velx = 0
        self.vely = 0
        self.move = False
        self.collide = False
        self.rapidez = 3
        self.timer_move = 0
        self.dir_ini = random.randrange(2)

        self.left_states = [self.imgs[1][0], self.imgs[1][1], self.imgs[1][2]]
        self.right_states = [self.imgs[2][0], self.imgs[2][1], self.imgs[2][2]]
        self.down_states = [self.imgs[0][0], self.imgs[0][1], self.imgs[0][2]]
        self.up_states = [self.imgs[3][0], self.imgs[3][1], self.imgs[3][2]]

    def update(self):
        if not self.move:
            self.behavior()
            self.image = pygame.transform.scale2x(self.imgs[self.fil][self.col])
        else:
            self.frame+=0.2
            if math.floor(self.frame)>2:
                    self.frame=0 
            if self.velx == -1:
                self.image = pygame.transform.scale2x(self.left_states[math.floor(self.frame)])
            if self.velx == 1:
                self.image = pygame.transform.scale2x(self.right_states[math.floor(self.frame)])
            if self.vely == -1:
                self.image = pygame.transform.scale2x(self.up_states[math.floor(self.frame)])
            if self.vely == 1:
                self.image = pygame.transform.scale2x(self.down_states[math.floor(self.frame)])


    def behavior(self):
        if random.randrange(100) > 95:
            direc = random.randrange(4) # valor entre [0,3] (4 direcciones)
            self.fil = direc
            self.col = 1

    def go_to(self, pos, dir_chg = True):
        x1 = pos[0]
        y1 = pos[1]

        x2 = self.rect.center[0]
        y2 = self.rect.center[1]

        if not dir_chg:
            self.dir_ini = 1

        if abs(x1 - x2) >= self.rapidez and abs(y1 - y2) >= self.rapidez:
            if self.timer_move == 10: # EN 10 CICLOS DECIDE SI CAMBIAR EL CAMINO
                self.timer_move = 0
                self.dir_ini = random.randrange(2)
            else:
                self.timer_move += 1
                if self.dir_ini == 1:
                    move_ent_x(self, pos)
                else:
                    move_ent_y(self, pos)
        elif abs(x1 - x2) < self.rapidez and abs(y1 - y2) >= self.rapidez:
            move_ent_y(self,pos)
        elif abs(x1 - x2) >= self.rapidez and abs(y1 - y2) < self.rapidez:
            move_ent_x(self,pos)
                                     
class Rival2(pygame.sprite.Sprite):
    def __init__(self, pos, dir_img):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = recorte(dir_img, (3, 4))
        self.fil = 0
        self.col = 1
        self.frame = 0.0
        self.image = pygame.transform.scale2x(self.imgs[self.fil][self.col])
        # self.image = self.imgs[self.fil][self.col]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vida = 100
        self.vel = [0,0,0,0]
        self.velx = 0
        self.vely = 0
        self.move = False
        self.collide = False
        self.rapidez = 3
        self.timer_move = 0
        self.dir_ini = random.randrange(2)
        self.timer_disp = 0

        self.left_states = [self.imgs[1][0], self.imgs[1][1], self.imgs[1][2]]
        self.right_states = [self.imgs[2][0], self.imgs[2][1], self.imgs[2][2]]
        self.down_states = [self.imgs[0][0], self.imgs[0][1], self.imgs[0][2]]
        self.up_states = [self.imgs[3][0], self.imgs[3][1], self.imgs[3][2]]

    def update(self):
        if not self.move:
            self.behavior()
            self.image = pygame.transform.scale2x(self.imgs[self.fil][self.col])
        else:
            self.frame+=0.2
            if math.floor(self.frame)>2:
                    self.frame=0 
            if self.velx == -1:
                self.image = pygame.transform.scale2x(self.left_states[math.floor(self.frame)])
            if self.velx == 1:
                self.image = pygame.transform.scale2x(self.right_states[math.floor(self.frame)])
            if self.vely == -1:
                self.image = pygame.transform.scale2x(self.up_states[math.floor(self.frame)])
            if self.vely == 1:
                self.image = pygame.transform.scale2x(self.down_states[math.floor(self.frame)])
    def behavior(self):
        if random.randrange(100) > 95:
            direc = random.randrange(4) # valor entre [0,3] (4 direcciones)
            self.fil = direc
            self.col = 1

    def go_to(self, pos, dir_chg = True):
        x1 = pos[0]
        y1 = pos[1]

        x2 = self.rect.center[0]
        y2 = self.rect.center[1]

        if not dir_chg:
            self.dir_ini = 1

        if abs(x1 - x2) >= self.rapidez and abs(y1 - y2) >= self.rapidez:
            if self.timer_move == 10: # EN 10 CICLOS DECIDE SI CAMBIAR EL CAMINO
                self.timer_move = 0
                self.dir_ini = random.randrange(2)
            else:
                self.timer_move += 1
                if self.dir_ini == 1:
                    move_ent_x(self, pos)
                else:
                    move_ent_y(self, pos)
        elif abs(x1 - x2) < self.rapidez and abs(y1 - y2) >= self.rapidez:
            move_ent_y(self,pos)
        elif abs(x1 - x2) >= self.rapidez and abs(y1 - y2) < self.rapidez:
            move_ent_x(self,pos)    

class Posion(pygame.sprite.Sprite):
    def __init__(self, pos):  
        pygame.sprite.Sprite.__init__(self)
        self.sheet = (pygame.transform.scale2x(pygame.image.load('graficos/Food.png')))
        self.sheet.set_clip(pygame.Rect([0+32*random.randrange(8),0+32*random.randrange(8), 32, 32]))   
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]

class Bloque(pygame.sprite.Sprite):
    def __init__(self, dim, pos, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale2x(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

class Bala2(pygame.sprite.Sprite):
    def __init__(self, pos_i, pos_f, color = BLANCO):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = pos_i[0]
        self.rect.y = pos_i[1]
        self.velx = 10
        self.calc_const(pos_i, pos_f)

    def calc_const(self, pos_i, pos_f):
        self.pi = pos_i
        self.pf = pos_f
        vec = [pos_f[0] - pos_i[0], pos_f[1] - pos_i[1]]
        if (pos_f[0]-pos_i[0]) == 0:
            self.a = 0
            self.angle = 0
        else:
            self.a = (pos_f[1]-pos_i[1]) / (pos_f[0]-pos_i[0])
            self.angle = math.atan(vec[1]/vec[0])
        x = pos_i[0]
        y = pos_i[1]
        self.b = y - (self.a * x)

    def update(self):
        if (self.pf[0] - self.pi[0]) == 0:
            self.rect.y += self.velx*math.cos(self.angle)
            self.rect.x = (self.a * self.rect.y) + self.b
        else:
            self.rect.x += self.velx*math.cos(self.angle)
            self.rect.y = (self.a * self.rect.x) + self.b

class Generador(pygame.sprite.Sprite):
    def __init__(self, pos, img):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((80, 80))
        # self.image.fill(color)
        # img = pygame.image.load(img)
        self.image = pygame.transform.scale2x(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.max_entities = 5
        self.entities = 0
        self.vida = 50
        self.temp = random.randrange(400, 700)

    def update(self):
        if self.entities <= self.max_entities:
            if self.temp >= 0:
                self.temp -= 1