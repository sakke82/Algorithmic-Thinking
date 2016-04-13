'''
Algorithmic Thinking (part1), programming assignment 1
directed graphs, https://class.coursera.org/algorithmicthink1-003/wiki/graph_degree 
Author: Sakari Hakala
'''

EX_GRAPH0 = {0:set([1,2]) , 1:set([]) , 2:set([]) }
EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]),
            8:set([1,2]), 9:set([0,3,4,5,6,7])}

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
