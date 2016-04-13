# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 23:11:36 2015

@author: aino
"""
import pickle
import matplotlib.pyplot as plt

with open('normal_time.txt', 'r') as f:
    normal_time = pickle.load(f)
    
with open('fast_time.txt', 'r') as f:
    fast_time = pickle.load(f)
    

plt.plot(normal_time, 'b', label = 'targeted_order')
plt.plot(fast_time, 'r', label = 'fast_targeted_order')
plt.legend(loc = 'upper left')
plt.title('Laptop Python 2.7 with Spyder')
plt.xlabel('Number of nodes (10x)')
plt.ylabel('Running time, seconds')
plt.savefig('app2_plot2.png')