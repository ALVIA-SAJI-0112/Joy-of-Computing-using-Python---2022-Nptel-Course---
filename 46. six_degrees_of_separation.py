# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:04:18 2022

@author: alvia
"""

import networkx as nx
import numpy

G=nx.read_edgelist("give the path of the file")
N=list(G.nodes())
spll=[] #to store the length of shortest path length list

for u in N: #u is a node
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest path between u and v is: ")
            spll.append(l)
            
min_spl=min(spll)
max_spl=max(spll)
avg_spl=numpy.avg(spll)

print("Minimun shortest path length",min_spl)
print("Max shortest path length",min_spl)
print("Avg shortest path length",avg_spl)