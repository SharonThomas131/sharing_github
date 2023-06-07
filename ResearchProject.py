#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

def graph(f, xl, xu, xlabel='x axis', ylabel='y axis', title='title', fig='plot.png', show=True):
    xp = (xu - xl) / 1000.0
    xpts = np.arange(xl, xu, xp)
    ypts = []
    for x in xpts:
        y = f(x)
        ypts.append(y)
    plt.plot(xpts, ypts)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(fig)
    if show: 
        plt.show()

def f(h):
    r = 0.9  # Radius value for the spherical tank
    V = (np.pi * h**2 * (3 * r - h)) / 3
    return V

graph(f, xl=0, xu=1, xlabel='h', ylabel='V', title='Volume of Liquid in Spherical Tank')


# In[ ]:




