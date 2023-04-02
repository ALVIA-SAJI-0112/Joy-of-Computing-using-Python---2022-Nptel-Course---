# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:16:03 2022

@author: alvia
"""

#people are nodes and edgesa re interactions between them
import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
l=[1,2,3] #list of nodes
G.add_nodes_from(1)
G=nx.complete_graph(10)

G=nx.gnp_random_graph(20,0.5) #giving probabality

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(1,3)
print(G.nodes())
print(G.edges())
nx.draw(G)
plt.show()