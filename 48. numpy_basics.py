# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:39:05 2022

@author: alvia
"""

import numpy as np
a=np.array([1,2,3])

print(type(a))
print(a.shape)
a=np.array([a[1],a[2],a[3]])
a[1]=6


a=np.array([1,2,3],[4,5,6])
print(a.shape)


a=np.zeros((2,2))
b=np.ones((2,2))
c=np.full((2,2),6)
d=np.random.random((2,2))
