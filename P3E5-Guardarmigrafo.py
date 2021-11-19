# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:57:49 2021

@author: Sangui
"""

import networkx as nx
#import geopandas as gps
import osmnx as ox
import numpy as no
from numpy import nan, isnan, logical_not
from itertools import product
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker

ox.config(use_cache=True, log_console=True)

G = nx.DiGraph()



G = ox.graph_from_bbox(
    north = -33.3637,
south = -33.56,
east = -70.5240,
west = -70.80,
network_type="drive",
clean_periphery=True,
custom_filter='["highway"~"motorway|primary|construction"]')

nx.write_gpickle(G,"santiago_grueso.gpickle")
