# -*- coding: utf-8 -*-
"""
Created on Tue Mon  15 21:34:58 2021

@author: Sangui
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
#from matplotlib.ticker import FormatStrFormatter
from math import sqrt
from networkx.algorithms import shortest_path

#PRIMER GRAFICO



G = nx.Graph()   

def costo(ni,nf,attr):
    fn_costo_arco = attr["costo"]
    flujo_arco = attr["flujo"]
    c= fn_costo_arco(flujo_arco)
    attr["Ccosto"]= c
    return c

f1 = lambda f: 10. + f/120.
f2 = lambda f: 14. + (3*f)/240.
f3 = lambda f: 10. + f/240.

#DEFINICION DE NOdOS

G.add_node("A", pos = [1,9] )
G.add_node("B", pos = [1,5] )
G.add_node("C", pos = [5,5] )
G.add_node("D", pos = [5,1] )
G.add_node("E", pos = [9,9] )
G.add_node("G", pos = [9,5] )


#FUNCION COSTO PARA ENTREGA 5 ---PROXIMAMENTE---------

#def fn_costo(q,p,L,k):
#    return ((L/v)+((u-5)*12)+(900/(u*p))*((10*q)-(u*p)+(sqrt(((10*q-u*p)**2)+(q/9))))
    

#Colores arcos
cafe, verde, gris = '#6C4E09', '#00701A', '#7C7C7C'

#DEFINICION ARCOS

G.add_edge("A","B", color= cafe ,weight=3, costo = f1,flujo=0, valor=0)
G.add_edge("E","G", color= cafe ,weight=3, costo = f1,flujo=0, valor=0)
G.add_edge("C","D", color= cafe ,weight=3, costo = f1,flujo=0, valor=0)
G.add_edge("B","C", color= verde ,weight=2.5, costo = f3,flujo=0, valor=0)
G.add_edge("C","G", color= verde ,weight=2.5, costo = f3,flujo=0, valor=0)
G.add_edge("A","C", color="b" ,weight=2, costo = f2,flujo=0, valor=0)
G.add_edge("B","D", color="b" ,weight=2, costo = f2,flujo=0, valor=0)
G.add_edge("C","E", color="b" ,weight=2, costo = f2,flujo=0, valor=0)
G.add_edge("D","G", color="b" ,weight=2, costo = f2,flujo=0, valor=0)



pos = nx.get_node_attributes(G,"pos")


labels = nx.get_edge_attributes(G,"costo")

for i in labels:
    if labels[i] ==f1:
        labels[i]= "f1= 10+ f/120"
    elif labels[i]==f2:
        labels[i]="f2= 14+ 3*f/240"
    elif labels[i]==f3:
        labels[i]="f3= 10+ f/240"
        
colores = nx.get_edge_attributes(G,'color').values()
weights = nx.get_edge_attributes(G,'weight').values()       

#def funcion_costo(ni, nf, atributos_arco):
	# print(f"ni = {ni} nf = {nf}, att={atributos_arco}")
#	return atributos_arco["costo"]





OD = { ("A","C") :1100, ("A","D") :1110, ("A","E") :1020, 
       ("B","C") :1140, ("B","D") :1160,("C","E") :1170, ("C","G") :1180,
      ("D","C") :350,  ("D","E") :1190, ("D","G") :1200 }
ODI = OD.copy()


for path in OD:
    origen =  path[0]
    destino = path[1]
    if ODI[path]/OD[path] <10:  #division de la demanda
        h= ODI[path]/100  #evaluando el cumplimiento de damanda sino involucrando el incremento
    else:
        h= ODI[path]/10000 # limite para actualizar valor h 
    rij = nx.algorithms.shortest_path(G, origen,destino, weight=costo)
    Nrutas = len(rij)
    
    for i in range(Nrutas-1):
        ni= rij[i]
        nj= rij[i+1]
        G.edges[ni,nj]["flujo"] +=h
        OD[path] -= h
    
flujos  = nx.get_edge_attributes(G,"flujo")

costos = nx.get_edge_attributes(G,"Ccosto")
        

    
#domx = plt.subplots()

plt.figure(0)
plt.suptitle("Red a resolver") #Grafico 1
plt.grid() #Aplica grilla

#Definimos ejes 
x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]

#Unidades de ejes
plt.xticks(x, x)
plt.yticks(y, y)

nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, width=2 , edge_color=colores)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.savefig("fig1_e4", bbox_inches = 'tight')
plt.show()


plt.figure(1)
plt.suptitle("Flujo en cada ruta r_ij") #GRAFICO 2
plt.grid()
x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]

#Unidades de ejes
plt.xticks(x, x)
plt.yticks(y, y)
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, width=2 , edge_color=colores)
nx.draw_networkx_edge_labels(G, pos, edge_labels=flujos)
plt.savefig("fig2_e4", bbox_inches = 'tight')
plt.show()

plt.figure(2)
plt.suptitle("Costo en cada ruta r_ij") #GRAFICO 3

plt.grid()
x = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]
y = [0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.]

#Unidades de ejes
plt.xticks(x, x)
plt.yticks(y, y)
nx.draw_networkx_nodes(G, pos=pos)
nx.draw_networkx_labels(G, pos=pos)
nx.draw_networkx_edges(G, pos, width=2 , edge_color=colores)
nx.draw_networkx_edge_labels(G, pos, edge_labels=costos)
plt.savefig("fig3_e4", bbox_inches = 'tight')
plt.show()
