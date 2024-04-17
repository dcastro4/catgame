import pygame
import random
import configparser

GREEN = (10, 215, 5)
RED = (255, 15, 15)
BLUE = (15, 100, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (100, 25, 120)
PINK = (225, 50, 225)
TEAL = (10, 205, 140)
YELLOW = (255, 250, 35)
GRAY = (127, 127, 127)
AQUA = (15, 245, 240)
ORANGE = (250, 130, 10)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

class Bloque(pygame.sprite.Sprite):
	def __init__(self, img, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

if __name__ == '__main__':
	print("Iniciando programa...")
	pygame.init()

	pantalla = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])

	bg_image = pygame.image.load('mapa02.png')

	fuente_mapa = configparser.ConfigParser()
	fuente_mapa.read('mapa.map')

	nom_archivo = fuente_mapa.get('general', 'archivo')


	fondos = pygame.image.load(nom_archivo)
	info_fondos = fondos.get_rect()

	bg_width = info_fondos[2]
	bg_height = info_fondos[3]

	sprts_colmns = int(fuente_mapa.get('general', 'sp_ancho'))
	sprts_flas = int(fuente_mapa.get('general', 'sp_alto'))
	desp_x = 32
	desp_y = 32
	matrix_imgs = list()

	# ENTIDADES
	bloques = pygame.sprite.Group()
	for i in range(sprts_flas):
		ls_imgs_fla = list()
		for j in range(sprts_colmns):
			cuadro = fondos.subsurface(j * desp_x, i * desp_y, 32, 32)
			ls_imgs_fla.append(cuadro)
		matrix_imgs.append(ls_imgs_fla)

	# ALGORITMO LECTURA MAPEO
	mapa = fuente_mapa.get('general', 'mapa')
	print('Mapa')
	print(mapa)
	ls_filas = mapa.split('\n')

	j = 0
	for fila in ls_filas:
		i = 0
		for columna in fila:
			if columna != '.':
				info = fuente_mapa.get(columna, 'info')
				fil = int(fuente_mapa.get(columna, 'fil'))
				col = int(fuente_mapa.get(columna, 'col'))
				print(columna, info, fil, col)
				bloque = Bloque(matrix_imgs[fil][col], (desp_x*i,desp_y*j))
				# pantalla.blit(matrix_imgs[fil][col], (desp_x*i,desp_y*j))
				bloques.add(bloque)
			i += 1
		j += 1

	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		pantalla.blit(bg_image, (0,0))
		bloques.draw(pantalla)
		pygame.display.flip()

	pygame.quit()
	print("Fin del programa")