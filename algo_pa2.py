# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:43:00 2015

Algorithmic Thinking (part1), programming assignment 2
Connected components and graph resilience,
https://class.coursera.org/algorithmicthink1-003/wiki/Programming_assignment_3
Author: Sakari Hakala
 """
from collections import deque  

def bfs_visited(ugraph, start_node):
    ''' input: ugraph -- undirected graph, start_node -- node of a graph
         output: a set of all visited nodes starting from stat_node using 
         breadth-first search algorithm             
    '''
    visited = set([start_node])
    queue = deque([start_node])
    while queue:
        node = queue.popleft()
        try:        
            for end_node in ugraph[node]:
                if end_node not in visited and end_node in ugraph.keys():
                    visited.add(end_node)
                    queue.append(end_node)
        except KeyError:
            pass
    return visited
         
def cc_visited(ugraph):
    ''' input: ugraph -- undirected graph
        output: list of sets, each set being connected component nodes
    '''
    nodes_left = set(ugraph.keys())
    connected = []
    while nodes_left:
        node = nodes_left.pop()
        visited = bfs_visited(ugraph, node)
        connected.append(visited)
        nodes_left = nodes_left.difference(visited)
    return connected
    
def largest_cc_size(ugraph):
    ''' input: undirected graph
        output: size of a largest connected components
    '''
    connected_components = cc_visited(ugraph)
    largest = 0
    for component in connected_components:
        if len(component) > largest:
            largest = len(component)
    return largest
    
def compute_resilience(ugraph, attack_order):
    ''' input: ugraph -- undirected graph,
        attack_order -- list of nodes in order to be removed
        output: list, with i'th element being largest connected component 
        after (i-1) node removed
    '''
    resilience = [largest_cc_size(ugraph)]
    for node in attack_order:
        del ugraph[node]
        resilience.append(largest_cc_size(ugraph))
    return resilience
