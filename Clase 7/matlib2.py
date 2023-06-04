# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:47:46 2023

@author: Chris
"""

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = np.log(x)

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)

ax.set(xlim=(0, 10), xticks=np.arange(1, 10),
       ylim=(0, 3), yticks=np.arange(1, 3))

plt.show()