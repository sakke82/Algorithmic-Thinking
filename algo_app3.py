# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:35:16 2015

@author: Sakari Hakala

Algorithmic Thinking, Application 1, part 3

"""

import random
import matplotlib.pyplot as plt
import numpy as np

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
        
    def get_node_numbers(self):
        print self._node_numbers
        
    def get_num_nodes(self):
        print self._num_nodes

'''
dpa = DPATrial(13)
dpa.get_num_nodes()
dpa.get_node_numbers()
for i in range(27770-13):
    print dpa.run_trial(13)
    dpa.get_num_nodes()
    dpa.get_node_numbers()
'''


def make_complete_graph(num_nodes):
    ''' Creates a complete graph with given number of nodes
    '''
    digraph = {}
    for start_node in range(0,num_nodes):
        digraph[start_node] = set([])
        for end_node in range(0,num_nodes):
            if start_node != end_node:
                digraph[start_node].add(end_node)
    return digraph
    
def compute_in_degrees(digraph):
    ''' Computes in degree of all nodes in given graph
    '''
    degrees = {}
    for key in digraph.keys():
        degrees[key] = 0
    for item in digraph.values():
        for end_node in item:
            degrees[end_node] += 1
    return degrees

def in_degree_distribution(digraph):
    ''' Computes distribution of in degrees in a given graph
    '''
    distribution = {}
    degrees = compute_in_degrees(digraph)
    for value in degrees.values():
        if value in distribution:
            distribution[value] += 1
        else:
            distribution[value] = 1
    return distribution
    
def sum_of_indegrees(graph):
    ''' Calculates the sum of in degree of all nodes
    '''
    totalindegrees = 0
    distribution = in_degree_distribution(graph)
    for key,value in distribution.iteritems():
        totalindegrees += key * value
    return totalindegrees

# First version
# 
#def make_digraph_dpa(n,m):
#    ''' Algorithm to create a digraph with n nodes, each having m out_degree
#    '''
#    digraph = make_complete_graph(m)
#    for new_node in range(m,n):
#        totindegrees = sum_of_indegrees(digraph)
#        #print totindegrees
#        nodes_subset = set([])
#        for item in range(0,m):   # select m nodes
#            in_node = random.randrange(0,new_node)
#            prob = (len(digraph[in_node])+1.) /(totindegrees + len(digraph))          
#            if random.random() < prob:
#                nodes_subset |= set([in_node])
#                #print 'ss', nodes_subset
#        digraph[new_node] = nodes_subset
#        
#    return digraph

def make_digraph_dpa(n,m):
    digraph = make_complete_graph(m)
    dpa = DPATrial(m)
    for new_node in range(m,n):
        new_node_neighbors = dpa.run_trial(m)
        digraph[new_node] = new_node_neighbors
    return digraph

#dpa_graph = make_digraph_dpa(27770,13)
dpa_graph = make_digraph_dpa(27770,13)
in_degrees = compute_in_degrees(dpa_graph)
distribution = in_degree_distribution(dpa_graph)
#print make_digraph_dpa(1000,50)
#print make_digraph_dpa(10000,100)
#print make_complete_graph(3)
#print sum_of_indegrees(make_complete_graph(3))

norm_values = []
keys = []

for key, value in in_degrees.iteritems():
    if key == 0:
        continue
    keys.append(np.log10(key))
    norm_values.append(np.log10(float(value)/27770))

plt.scatter(keys,norm_values)
plt.suptitle('in degree distribution, normalized.', fontsize = 20)
plt.xlabel('number of edges, log10', fontsize = 12)
plt.ylabel('frequency, log10', fontsize = 12)
plt.show()