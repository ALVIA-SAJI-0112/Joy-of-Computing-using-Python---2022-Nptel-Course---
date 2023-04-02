# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 17:46:35 2022

@author: alvia
"""

import numpy as np
x=np.array([1,2],dtype=np.int64)
print(x.dtype)

import numpy as np
x=np.array([1,2],[3,4],dtype=np.float64)
y=np.array([5,6],[7,8],dtype=np.float64)
print(x.dtype)
print(y.dtype)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.(x/y))
print(np.sqrt(y))
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))
print(x)
print(x.T)