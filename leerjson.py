import json

nom_archivo = "mapa/mapa.json"
with open(nom_archivo) as archivo:
	datos = json.load(archivo)

capas = datos["layers"]

mapa = capas[2]["data"]
limite = capas[1]["width"]
print(limite, type(limite))

cont = 0
txt = ""
for elem in mapa:
	txt += " " + str(elem)
	cont += 1
	if cont >= limite:
		print(txt)
		print("")
		txt = ""
		cont = 0