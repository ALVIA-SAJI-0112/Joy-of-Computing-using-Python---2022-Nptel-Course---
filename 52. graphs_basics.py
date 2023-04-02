# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:22:38 2022

@author: alvia
"""

#in console
import networkx as nx
nx.barbell_graph(4,2)
G=nx.barell_graph(4,2)
nx.draw(G)
G=nx.barell_graph(4,3)
nx.draw(G)
G=nx.complete_graph(4)
nx.draw(G)
G=nx.cycle_graph(5)
nx.draw(G)
G=nx.ladder_graph(5)
nx.draw(G)
G=nx.ladder_(5)
G=nx.path_graph(5)
nx.draw(G)
G=nx.star_graph(5)
nx.draw(G)
G=nx.wheel_graph(5)
nx.draw(G)
G=nx.gnp_random_graph(5,0.5)
nx.draw(G)