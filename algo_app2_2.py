# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:13:02 2015

@author: aino
"""
import time
import algo_app2_1 as app2
import alg_application2_provided as provided
import algo_pa2 as pa2
import pickle

create_upas = []
normal_time = []
fast_time = []

for n in range(10,1000,10):
    print n
    t0 = time.time()
    upa = app2.create_UPA(n,5)
    create_upas.append(time.time() - t0)
    #print upa
    use_graph = provided.copy_graph(upa)

        
    t0 = time.time()
    order = provided.targeted_order(use_graph)
    #normal_resilience = pa2.compute_resilience(use_graph, order)
    #normal_resilience = app2.attack(upa, 'normal')
    normal_time.append(time.time() - t0)
    
    use_graph = provided.copy_graph(upa)
    
    t0 = time.time()
    order = app2.fastTargetedOrder(use_graph)
    #fast_resilience = pa2.compute_resilience(use_graph, order)
    #fast_resilience = app2.attack(upa, 'fast')
    fast_time.append(time.time() - t0)   

for i in range(len(normal_time)):
    print 'Time for upa creation :', create_upas[i] 
    print 'Normal attack time: ', normal_time[i] 
    print 'Fast attack time: ', fast_time[i]
    print normal_time[i] > fast_time[i]
    print '***********'
    
pickle.dump(normal_time, open('normal_time.txt','w'))
pickle.dump(fast_time, open('fast_time.txt','w'))