# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:45:47 2021

@author: Sangui
"""




import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
from math import sqrt


#PRIMER GRAFICO



G = nx.Graph()   

G.add_node("0", pos = [1,2] )
G.add_node("1", pos = [4,3] )
G.add_node("2", pos = [1,6] )
G.add_node("3", pos = [7,3] )
G.add_node("4", pos = [10,1] )
G.add_node("5", pos = [0,10] )
G.add_node("6", pos = [4,0] )
G.add_node("7", pos = [5,8] )
G.add_node("8", pos = [9,7] )
G.add_node("9", pos = [8,10] )


#Colores arcos
cafe, verde, gris = '#6C4E09', '#00701A', '#7C7C7C'

#DEFINICION ARCOS

G.add_edge("0","1", color= cafe ,weight=2)
G.add_edge("0","2", color=gris ,weight=2)
G.add_edge("0","6", color=gris ,weight=2)
G.add_edge("1","2", color= cafe ,weight=2)
G.add_edge("1","3", color= verde ,weight=2)
G.add_edge("1","7", color= cafe ,weight=2)
G.add_edge("2","5", color= cafe ,weight=2)
G.add_edge("3","4", color= verde ,weight=2)
G.add_edge("3","6", color= cafe ,weight=2)
G.add_edge("3","7", color= verde ,weight=2)
G.add_edge("3","8", color= cafe ,weight=2)
G.add_edge("4","6", color=gris ,weight=2)
G.add_edge("4","8", color=gris ,weight=2)
G.add_edge("5","7", color=gris ,weight=2)
G.add_edge("7","9", color= verde ,weight=2)
G.add_edge("8","9", color= verde ,weight=2)




pos = nx.get_node_attributes(G, "pos")


colores = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()


fig, domx = plt.subplots()



nx.draw(G, pos, edge_color=colores, width=list(weights), with_labels=True)
limits=plt.axis('on') 
domx.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)



x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]


plt.xticks(x, x)
plt.yticks(y, y)
domx.grid()
domx.set_xlabel("X [km]")
domx.set_ylabel("Y [km]")

plt.savefig("fig1", bbox_inches = 'tight')
plt.show()


#SEGUNDO GRAFICO



G = nx.Graph()   

G.add_node("0", pos=[1,2])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])


#DEFINICION ARCOS

G.add_edge("0","1", costo=(sqrt(((3-2)**2)+((4-1)**2)))/40)
G.add_edge("0","2", costo=(sqrt(((6-2)**2)+((1-1)**2)))/120)
G.add_edge("0","6", costo=(sqrt(((0-2)**2)+((4-1)**2)))/120)
G.add_edge("1","2", costo=(sqrt(((6-3)**2)+((1-4)**2)))/40)
G.add_edge("1","7", costo=(sqrt(((8-3)**2)+((5-4)**2)))/40)  
G.add_edge("1","3",weight=2, costo=(sqrt(((3-3)**2)+((7-4)**2)))/60) 
G.add_edge("2","5", costo=(sqrt(((10-6)**2)+((0-1)**2)))/40) 
G.add_edge("3","4", costo=(sqrt(((1-3)**2)+((10-7)**2)))/60)
G.add_edge("3","6", costo=(sqrt(((0-3)**2)+((4-7)**2)))/40)
G.add_edge("3","7", costo=(sqrt(((8-3)**2)+((5-7)**2)))/60)
G.add_edge("3","8", costo=(sqrt(((7-3)**2)+((9-7)**2)))/40)
G.add_edge("4","8", costo=(sqrt(((7-1)**2)+((9-10)**2)))/120)
G.add_edge("4","6", costo=(sqrt(((0-1)**2)+((4-10)**2)))/120)
G.add_edge("5","7", costo=(sqrt(((8-10)**2)+((5-0)**2)))/120)
G.add_edge("7","9", costo=(sqrt(((10-8)**2)+((9-5)**2)))/60)
G.add_edge("8","9", costo=(sqrt(((10-7)**2)+((8-9)**2)))/60)


pos = nx.get_node_attributes(G, "pos")



weights = nx.get_edge_attributes(G,'weight').values()

labels = nx.get_edge_attributes(G,"costo")


def funcion_costo(ni, nf, atributos_arco):
	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
	return atributos_arco["costo"]


# path = nx.shortest_path(G, source="A", target="D", weight="costo")
# path = nx.dijkstra_path(G, source="A", target="D", weight="costo")
ruta = nx.dijkstra_path(G, source="0", target="9", weight=funcion_costo)
#ruta2 = nx.dijkstra_path(G, source="4", target="5", weight=funcion_costo)
#ruta3 = nx.dijkstra_path(G, source="0", target="4", weight=funcion_costo)
costo_ruta = 0.
Nparadas = len(ruta)

print(f"Ruta Nparadas={Nparadas} ruta: {ruta}")
for i in range(Nparadas-1):
	parada_i = ruta[i]
	parada_f = ruta[i+1]
	costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
	print(f"Tramo {i}  {parada_i} a {parada_f} costo={costo_tramo_i}")
	costo_ruta += costo_tramo_i

print(f"Costo de ruta = {costo_ruta}")



# edgelist = [\
# 	("A","B"),
# 	("C","D"),
# 	]

# colores = [\
# "r",
# "k"
# ]

colores = []
edgelist = []
for ni, nf in G.edges:
	if ni in ruta and nf in ruta:
		colores.append("r")
	else:
		colores.append("k")

	edgelist.append((ni,nf))
	# print(f"{ni} {nf} esta_en_la_ruta: {esta_en_la_ruta}")

fig, domx = plt.subplots()



nx.draw(G, pos, edge_color=colores, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
domx.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)



x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]



plt.xticks(x, x)
plt.yticks(y, y)
domx.grid()
domx.set_xlabel("X [km]")
domx.set_ylabel("Y [km]")
plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
plt.savefig("fig2", bbox_inches = 'tight')
plt.show()

#TERCERO GRAFICO



G = nx.Graph()   

G.add_node("0", pos=[1,2])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])


#DEFINICION ARCOS

G.add_edge("0","1", costo=(sqrt(((3-2)**2)+((4-1)**2)))/40)
G.add_edge("0","2", costo=(sqrt(((6-2)**2)+((1-1)**2)))/120)
G.add_edge("0","6", costo=(sqrt(((0-2)**2)+((4-1)**2)))/120)
G.add_edge("1","2", costo=(sqrt(((6-3)**2)+((1-4)**2)))/40)
G.add_edge("1","7", costo=(sqrt(((8-3)**2)+((5-4)**2)))/40)  
G.add_edge("1","3",weight=2, costo=(sqrt(((3-3)**2)+((7-4)**2)))/60) 
G.add_edge("2","5", costo=(sqrt(((10-6)**2)+((0-1)**2)))/40) 
G.add_edge("3","4", costo=(sqrt(((1-3)**2)+((10-7)**2)))/60)
G.add_edge("3","6", costo=(sqrt(((0-3)**2)+((4-7)**2)))/40)
G.add_edge("3","7", costo=(sqrt(((8-3)**2)+((5-7)**2)))/60)
G.add_edge("3","8", costo=(sqrt(((7-3)**2)+((9-7)**2)))/40)
G.add_edge("4","8", costo=(sqrt(((7-1)**2)+((9-10)**2)))/120)
G.add_edge("4","6", costo=(sqrt(((0-1)**2)+((4-10)**2)))/120)
G.add_edge("5","7", costo=(sqrt(((8-10)**2)+((5-0)**2)))/120)
G.add_edge("7","9", costo=(sqrt(((10-8)**2)+((9-5)**2)))/60)
G.add_edge("8","9", costo=(sqrt(((10-7)**2)+((8-9)**2)))/60)

# Coordenadas de los nodos
pos = nx.get_node_attributes(G, "pos")



weights = nx.get_edge_attributes(G,'weight').values()

labels = nx.get_edge_attributes(G,"costo")


def funcion_costo(ni, nf, atributos_arco):
	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
	return atributos_arco["costo"]


# path = nx.shortest_path(G, source="A", target="D", weight="costo")
# path = nx.dijkstra_path(G, source="A", target="D", weight="costo")
ruta = nx.dijkstra_path(G, source="4", target="5", weight=funcion_costo)
#ruta2 = nx.dijkstra_path(G, source="4", target="5", weight=funcion_costo)
#ruta3 = nx.dijkstra_path(G, source="0", target="4", weight=funcion_costo)
costo_ruta = 0.
Nparadas = len(ruta)

print(f"Ruta Nparadas={Nparadas} ruta: {ruta}")
for i in range(Nparadas-1):
	parada_i = ruta[i]
	parada_f = ruta[i+1]
	costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
	print(f"Tramo {i}  {parada_i} a {parada_f} costo={costo_tramo_i}")
	costo_ruta += costo_tramo_i

print(f"Costo de ruta = {costo_ruta}")



# edgelist = [\
# 	("A","B"),
# 	("C","D"),
# 	]

# colores = [\
# "r",
# "k"
# ]

colores = []
edgelist = []
for ni, nf in G.edges:
	if ni in ruta and nf in ruta:
		colores.append("r")
	else:
		colores.append("k")

	edgelist.append((ni,nf))
	# print(f"{ni} {nf} esta_en_la_ruta: {esta_en_la_ruta}")

fig, domx = plt.subplots()



nx.draw(G, pos, edge_color=colores, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
domx.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)



x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]



plt.xticks(x, x)
plt.yticks(y, y)
domx.grid()
domx.set_xlabel("X [km]")
domx.set_ylabel("Y [km]")
plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
plt.savefig("fig3", bbox_inches = 'tight')
plt.show()

#CUARTO GRAFICO



G = nx.Graph()   #Graph asume bidireccionalidad en todos los arcos

G.add_node("0", pos=[1,2])
G.add_node("1", pos=[4,3])
G.add_node("2", pos=[1,6])
G.add_node("3", pos=[7,3])
G.add_node("4", pos=[10,1])
G.add_node("5", pos=[0,10])
G.add_node("6", pos=[4,0])
G.add_node("7", pos=[5,8])
G.add_node("8", pos=[9,7])
G.add_node("9", pos=[8,10])




G.add_edge("0","1", costo=(sqrt(((3-2)**2)+((4-1)**2)))/40)
G.add_edge("0","2", costo=(sqrt(((6-2)**2)+((1-1)**2)))/120)
G.add_edge("0","6", costo=(sqrt(((0-2)**2)+((4-1)**2)))/120)
G.add_edge("1","2", costo=(sqrt(((6-3)**2)+((1-4)**2)))/40)
G.add_edge("1","7", costo=(sqrt(((8-3)**2)+((5-4)**2)))/40)  
G.add_edge("1","3",weight=2, costo=(sqrt(((3-3)**2)+((7-4)**2)))/60) 
G.add_edge("2","5", costo=(sqrt(((10-6)**2)+((0-1)**2)))/40) 
G.add_edge("3","4", costo=(sqrt(((1-3)**2)+((10-7)**2)))/60)
G.add_edge("3","6", costo=(sqrt(((0-3)**2)+((4-7)**2)))/40)
G.add_edge("3","7", costo=(sqrt(((8-3)**2)+((5-7)**2)))/60)
G.add_edge("3","8", costo=(sqrt(((7-3)**2)+((9-7)**2)))/40)
G.add_edge("4","8", costo=(sqrt(((7-1)**2)+((9-10)**2)))/120)
G.add_edge("4","6", costo=(sqrt(((0-1)**2)+((4-10)**2)))/120)
G.add_edge("5","7", costo=(sqrt(((8-10)**2)+((5-0)**2)))/120)
G.add_edge("7","9", costo=(sqrt(((10-8)**2)+((9-5)**2)))/60)
G.add_edge("8","9", costo=(sqrt(((10-7)**2)+((8-9)**2)))/60)

# Coordenadas de los nodos
pos = nx.get_node_attributes(G, "pos")



weights = nx.get_edge_attributes(G,'weight').values()

labels = nx.get_edge_attributes(G,"costo")


def funcion_costo(ni, nf, atributos_arco):
	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
	return atributos_arco["costo"]


# path = nx.shortest_path(G, source="A", target="D", weight="costo")
# path = nx.dijkstra_path(G, source="A", target="D", weight="costo")
ruta = nx.dijkstra_path(G, source="0", target="4", weight=funcion_costo)
#ruta2 = nx.dijkstra_path(G, source="4", target="5", weight=funcion_costo)
#ruta3 = nx.dijkstra_path(G, source="0", target="4", weight=funcion_costo)
costo_ruta = 0.
Nparadas = len(ruta)

print(f"Ruta Nparadas={Nparadas} ruta: {ruta}")
for i in range(Nparadas-1):
	parada_i = ruta[i]
	parada_f = ruta[i+1]
	costo_tramo_i = G.edges[parada_i, parada_f]["costo"]
	print(f"Tramo {i}  {parada_i} a {parada_f} costo={costo_tramo_i}")
	costo_ruta += costo_tramo_i

print(f"Costo de ruta = {costo_ruta}")



# edgelist = [\
# 	("A","B"),
# 	("C","D"),
# 	]

# colores = [\
# "r",
# "k"
# ]

colores = []
edgelist = []
for ni, nf in G.edges:
	if ni in ruta and nf in ruta:
		colores.append("r")
	else:
		colores.append("k")

	edgelist.append((ni,nf))
	# print(f"{ni} {nf} esta_en_la_ruta: {esta_en_la_ruta}")

fig, domx = plt.subplots()



nx.draw(G, pos, edge_color=colores, width=list(weights), with_labels=True)
limits=plt.axis('on') # turns on axis
domx.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)



x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]



plt.xticks(x, x)
plt.yticks(y, y)
domx.grid()
domx.set_xlabel("X [km]")
domx.set_ylabel("Y [km]")
plt.suptitle(f"Ruta minima: {ruta} costo={costo_ruta}")
plt.savefig("fig4", bbox_inches = 'tight')
plt.show()