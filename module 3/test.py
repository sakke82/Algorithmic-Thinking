# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:52:04 2015

@author: aino
"""
import alg_cluster
import cluster as cl

print cl.closest_pair_strip([alg_cluster.Cluster(set([]), 0, 0, 1, 0), 
                              alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
                            alg_cluster.Cluster(set([]), 2, 0, 1, 0), 
                            alg_cluster.Cluster(set([]), 3, 0, 1, 0)], 
                            1.5, 1.0)
                        
print cl.closest_pair_strip([alg_cluster.Cluster(set([]), 0.32, 0.16, 1, 0), alg_cluster.Cluster(set([]), 0.39, 0.4, 1, 0), alg_cluster.Cluster(set([]), 0.54, 0.8, 1, 0), alg_cluster.Cluster(set([]), 0.61, 0.8, 1, 0), alg_cluster.Cluster(set([]), 0.76, 0.94, 1, 0)], 0.46500000000000002, 0.070000000000000007)

print cl.fast_closest_pair([alg_cluster.Cluster(set([]), 0, 0, 1, 0), 
                         alg_cluster.Cluster(set([]), 1, 0, 1, 0), 
                        alg_cluster.Cluster(set([]), 2, 0, 1, 0), 
                        alg_cluster.Cluster(set([]), 3, 0, 1, 0)])