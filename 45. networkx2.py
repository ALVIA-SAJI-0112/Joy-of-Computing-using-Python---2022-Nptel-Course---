# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:26:34 2022

@author: alvia
"""

import networkx as nx
import matplotlib.pyplot as plt

G=nx.gnp_random_graph(50,0.3)
nx.draw(G)
plt.show()

#in console
G.nodes()
print(G.nodes())
print(G.edges())
print(G.degree(0))

#another type of graph
G=nx.barabasi_albert_graph(50,2)
nx.draw(G)
plt.show()

nx.write_gexf(G,"analysis1.gexf")