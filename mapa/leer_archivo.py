import configparser

fuente_mapa = configparser.ConfigParser()
fuente_mapa.read('mapa.map')
print(fuente_mapa.sections())
print(fuente_mapa.items('#'))
print(fuente_mapa.get('.', 'info'))

mapa = fuente_mapa.get('general', 'mapa')
print('Mapa')
print(mapa)
ls_filas = mapa.split('\n')

print(ls_filas)
for columna in ls_filas[0]:
	info = fuente_mapa.get(columna, 'info')
	fil = fuente_mapa.get(columna, 'fil')
	col = fuente_mapa.get(columna, 'col')
	print(columna, info, fil, col)
