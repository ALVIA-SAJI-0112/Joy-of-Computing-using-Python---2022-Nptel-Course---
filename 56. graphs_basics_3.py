# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 23:47:36 2022

@author: alvia
"""

#in console
import networkx as nx
U=nx.Graph() #undirected graph
G=nx.DiGraph()
G.nodes ()
NodeView( ())
G. add_nodes_from([i for i in range(5)])
G.nodes()
NodeView((0,1,2,3,4))
list(G.nodes())
G.out_edges()
OutEdgeView([1,2])
G.in_edges()
InEdgeView([1,2])
G.add_edge(1,2)
G.in_edges(1)
InEdgeDataView([])
G.add_edge(0,3)
G.add_edge(2,3)
G.add_edge(3,2)
G.add_edge(4,1)
list(G.out_edges(3))
list(G.in_edges(3))
