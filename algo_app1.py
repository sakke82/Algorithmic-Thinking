'''
Algorithmic Thinking (part1), application 1
directed graphs, citations of scientific papers
https://class.coursera.org/algorithmicthink1-003/human_grading/view/courses/975649/assessments/31/submissions
Author: Sakari Hakala
'''

import urllib2
import matplotlib.pyplot as plt
import numpy as np

# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

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

citation_graph = load_graph(CITATION_URL)
in_degrees = in_degree_distribution(citation_graph)

degrees = compute_in_degrees(citation_graph)
#print np.mean(degrees.values()) # AVG = 12.7

'''
norm_values = []
keys = []

for key, value in in_degrees.iteritems():
    keys.append(np.log10(key))
    norm_values.append(np.log10(float(value)/27770))

plt.scatter(keys,norm_values)
plt.suptitle('in degree distribution, normalized.', fontsize = 20)
plt.xlabel('number of citations, log10', fontsize = 12)
plt.ylabel('frequency, log10', fontsize = 12)
plt.show()
'''