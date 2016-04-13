# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:38:30 2015

Algorithmic Thinking (part1), programming application  2
Connected components and graph resilience,
https://class.coursera.org/algorithmicthink1-003/human_grading/view/courses/975649/assessments/32/submissions
Author: Sakari Hakala

"""

import alg_application2_provided as provided
import algo_pa2 as pa2
import random
import matplotlib
#matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import pickle
import time

#computer_network = provided.load_graph(provided.NETWORK_URL)

def make_complete_graph(num_nodes):
    ''' Creates a complete graph with given number of nodes
    '''
    graph = {}
    for start_node in range(0,num_nodes):
        graph[start_node] = set([])
        for end_node in range(0,num_nodes):
            if start_node != end_node:
                graph[start_node].add(end_node)
    return graph
    
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

def number_of_connections(graph_distribution):
    connections = 0    
    for key, value in graph_distribution.iteritems():
        connections += key* value
    return connections/ 2

# create an undirected graph with ER -algorithm
def undirected_ER(number_nodes, probability):
    ''' input: number_nodes -- number of the nodes in a graph, probability -- 
        probability of each pair of node to have edge
        output: a undirected graph presented as a dictionary    
    '''
    ugraph = {}
    for node in range(number_nodes):
        ugraph[node] = set([])
    for node in range(number_nodes):
        for connection in range(number_nodes):
            if node == connection:
                continue
            rand = random.random()
            if rand < probability/2.:
                ugraph[node].add(connection)
                ugraph[connection].add(node)
    return ugraph
    
def create_UPA(number_nodes, initial_nodes):
    graph = make_complete_graph(initial_nodes)
    upa = provided.UPATrial(initial_nodes)
    for new_node in range(initial_nodes,number_nodes):
        new_node_neighbors = upa.run_trial(initial_nodes)
        graph[new_node] = new_node_neighbors
        for node in new_node_neighbors:
            graph[node].add(new_node)
    return graph


# Create undirected ER-graph with 1239 nodes and (1239 C 2)*0.004 edges    
#uer = undirected_ER(1239,0.004)
#dist =  in_degree_distribution(uer)
#print number_of_connections(dist)

#upa = create_UPA(1239,2)
#dist_upa = in_degree_distribution(upa)
#print number_of_connections(dist_upa)        

def plot_graph_degrees(graph):
    in_degrees = compute_in_degrees(graph)
    norm_values = []
    keys = []
    
    for key, value in in_degrees.iteritems():
        if key == 0:
            continue
        keys.append(key)
        norm_values.append(float(value)/len(in_degrees.keys()))
    
    plt.scatter(keys,norm_values)
    plt.suptitle('in degree distribution, normalized.', fontsize = 20)
    plt.xlabel('number of edges', fontsize = 12)
    plt.ylabel('frequency', fontsize = 12)
    plt.show()
    
#plot_graph_degrees(uer)
#plot_graph_degrees(computer_network)
#plot_graph_degrees(upa)
    
def random_order(graph):
    ''' input: graph -- undirected or directed graph
        output: list of nodes in a graph in a random order
    '''
    nodes = graph.keys()
    random.shuffle(nodes)
    return nodes

def random_attack(graph):
    '''
    '''
    
    attack_order = random_order(graph)
    graph_resilience = pa2.compute_resilience(graph, attack_order)
    return graph_resilience

#print random_attack(computer_network)
#print random_order(computer_network)
#print random_order(uer)
#uer_resilience = random_attack(uer)
#with open('uer.txt', 'r') as f:
#    uer_resilience = pickle.load(f)
#
##upa_resilience = random_attack(upa)
#with open('upa.txt', 'r') as f:
#    upa_resilience = pickle.load(f)
#    
##cn_resilience = random_attack(computer_network)
#with open('cn.txt', 'r') as f:
#    cn_resilience = pickle.load(f)
#   
#plt.plot(range(0,1240), uer_resilience, '-b', label = 'uER, p = 0.004')
#plt.plot(range(0,1240), upa_resilience, '-r', label = 'UPA, m = 2')
#plt.plot(range(0,1240), cn_resilience, '-c', label = 'computer network')
#plt.legend(loc='upper right')
#plt.savefig('app2_plot1.png')

def fastTargetedOrder(graph):
    ''' input : graph -- a graph
        output: a list, of nodes in decreasing order of their degrees   
    ''' 
    new_graph = provided.copy_graph(graph)
    number_nodes = len(new_graph.keys())
    degree_sets = []
    for dummy in range(number_nodes):
        degree_sets.append(set([]))
    for node in new_graph.keys():
        #print node, new_graph[node]
        degree = len(new_graph[node])
        #print degree
        degree_sets[degree].update([node])
        #print  '*****'
    #for item in degree_sets:
        #print item
    order = []
    for degree in range(number_nodes -1, -1, -1):
        #print 'Degree: ', degree
        while degree_sets[degree]:
            #print new_graph
            node = degree_sets[degree].pop()
            #print type(new_graph[node])
            #print new_graph#[node]
            for neighbor in new_graph[node]:
                neighbor_degree = len(new_graph[neighbor])
                degree_sets[neighbor_degree].remove(neighbor)
                degree_sets[neighbor_degree - 1].update([neighbor])
            order.append(node)
            provided.delete_node(new_graph,node)
    return order
    
def attack(graph, attack_type):
    new_graph = provided.copy_graph(graph)
    if attack_type == 'normal':
        order = provided.targeted_order(new_graph)
    elif attack_type == 'fast':
        order = fastTargetedOrder(new_graph)
    resilience = pa2.compute_resilience(new_graph, order)
    return resilience
    
#t0 = time.time()
#normal_resilience = attack(upa, 'normal') 
#normal_time = time.time() - t0
#
#t0 = time.time()
#fast_resilience = attack(upa, 'fast')
#fast_time = time.time() - t0   
##
#print 'Normal attack time: ', normal_time
#print 'Fast attack time: ', fast_time
    
#print fastTargetedOrder(create_UPA(25,3))