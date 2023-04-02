# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 08:53:17 2022

@author: alvia
"""

import networkx as nx
import matplotlib.pyplot as plt
G=nx. read_edgelist(r"/Users/simransetia/Desktop/page_rank. txt", create_using=nx.DiGraph(),nodetype=int)
nx.draw(G,with_labels=True)
plt.show()