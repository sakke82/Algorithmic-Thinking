import random

def random_digraph(num_nodes, p):
    digraph = {}
    for node in range(num_nodes):
        digraph[node] = set([])
    for start_node in range(num_nodes):
        for end_node in range(num_nodes):
            if start_node != end_node:
                a = random.random()
                if a < p:
                    digraph[start_node] |= set([end_node])
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

#print random_digraph(3,1)
g = random_digraph(1000,.5)
print in_degree_distribution(g)

gg = random_digraph(1000,.3)
print in_degree_distribution(gg)
