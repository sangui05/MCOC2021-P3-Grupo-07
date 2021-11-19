# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 17:06:13 2021

@author: Sangui
"""

import networkx as nx
#import geopandas as gps
import osmnx as ox
import numpy as no
from numpy import nan, isnan, logical_not
from itertools import product
import matplotlib.pyplot as plt
import geopandas as gps

zonas_gdf=gps.read_file("zonas-eod.json")

G = nx.read_gpickle("santiago_grueso.gpickle")


ox.config(use_cache=True, log_console=True)

gdf_nodes, gdf_edges= ox.graph_to_gdfs(G)

street_centroids = gdf_edges.centroid

print (zonas_gdf)
print(f"gdf_nodes={gdf_nodes}")
print(f"gdf_edges={gdf_edges}")

plt.figure()

ax=plt.subplot(111)

#gdf_nodes.plot(column="street_count", ax=ax, legend=True)
gdf_edges[gdf_edges.highway== "motorway"].plot(ax=ax, color="orange")
gdf_edges[gdf_edges.highway== "primary"].plot(ax=ax, color="blue")
gdf_edges[gdf_edges.highway=="construction"].plot(ax=ax, color="red")
gdf_edges[gdf_edges.name=="Americo Vespucio Oriente"].plot(ax=ax, color="red", linewidth=4)


#gdf_edges[gdf_edges.highway.construction== "motorway"].plot(ax=ax, color="red")



zona_origen = 181
zona_destino = 677

nodo_origen = 2744834665
nodo_destino = 1225556707

#--------------LO COMENTADO RECORRE NODOS DE FORMA OD---------------
#i=0
#nodo_origen=G.nodes[i]
#nodo_destino=G.nodes[i+1]
#while i<= len(G.nodes):
#    nodo_origen=G.nodes[i]
#    nodo_destino=G.nodes[i+1]
#    i+=1
    
#-----------------------------------------------------------------------
zonas_gdf[zonas_gdf.ID==zona_origen].plot(ax=ax, color="#9D9D9D")
zonas_gdf[zonas_gdf.ID==zona_destino].plot(ax=ax, color="#9D9D9D")

#for i, node in enumerate(G.nodes):
    #ax.annotate(s=str(node), xy=(G.nodes[node]["x"],G.nodes[node]["y"]), horizontalalignment="center")
ax.annotate(s=str(nodo_origen), xy=(G.nodes[nodo_origen]["x"],G.nodes[nodo_origen]["y"]))
ax.annotate(s=str(nodo_destino), xy=(G.nodes[nodo_destino]["x"],G.nodes[nodo_destino]["y"]))

from networkx.algorithms import astar_path,all_simple_paths, all_shortest_paths, dijkstra_path

def weightfun(n1, n2, attr_arco):
    
    usar_arco_numero=0
    if "name" in attr_arco[usar_arco_numero]:
        name = attr_arco[usar_arco_numero]["name"]
    else: 
        name= ""
    length = attr_arco[usar_arco_numero]["length"]
    street_type = attr_arco[usar_arco_numero]["highway"]
    
    if street_type=="motorway":
        vel = 25
    elif street_type=="primary":
        vel = 15
    elif street_type=="secondary":
        vel = 15
    else:
        vel = 8
    tiempo = length/vel
    costo = tiempo
    return costo




take_path = dijkstra_path(G,nodo_origen,nodo_destino)



#print(take_path)

Nparadas=len(take_path)

arcos_a_eliminar=[]


for i_parada in range(Nparadas-1):
    n1 = take_path[i_parada]
    n2 = take_path[i_parada+1]
    
    tomar_arco = 0
    arco = G.edges[n1,n2,tomar_arco]
    if"name"in arco:
        nombre = arco["name"]
    else:
        nombre = ""
    nombre = arco["name"]
    #print (f"Uniendo {n1} con {n2} Sigue por {nombre}")
    #print(f"   Info arco {arco}")
    
    xx = [G.nodes[n1]["x"],G.nodes[n2]["x"]]
    yy = [G.nodes[n1]["y"],G.nodes[n2]["y"]]
    
    
    #[(a,b) for a, b, attrs in G.edges(data=True) if attrs["weight"] >= 500]
    if not arco["name"] == "Americo Vespucio Oriente" or "Avenida Ossa":
        arcos_a_eliminar.append(arco)
   

    ax.plot(xx,yy, color="#F5A800",linewidth=3)

G.remove_edges_from(arcos_a_eliminar) 

plt.show()
 