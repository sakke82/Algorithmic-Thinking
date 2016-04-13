
"""
Created on Tue Oct 20 08:43:41 2015

@author: Sakari Hakala

Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    
    num_of_clusters = len(cluster_list)
    
    min_dist_pair = None
    
    for index1 in range(num_of_clusters - 1):
        for index2 in range(index1 +1, num_of_clusters):
            dist = pair_distance(cluster_list, index1, index2)            
            if min_dist_pair == None or dist[0] < min_dist_pair[0]:
                min_dist_pair = dist
    
    return min_dist_pair



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    
    num_of_clusters = len(cluster_list)

    if num_of_clusters <= 3:
        return slow_closest_pair(cluster_list)
    
    mid_point = int(math.floor(num_of_clusters / 2))
    left = cluster_list[::mid_point]
    right = cluster_list[mid_point::]
    min_dist_left = fast_closest_pair(left)
    min_dist_right = fast_closest_pair(right)
    
    if min_dist_left[0] <= min_dist_right[0]:
        min_dist = min_dist_left
    else:
        min_dist = min_dist_right
    
    mid_strip = (cluster_list[mid_point -1].horiz_center() + cluster_list[mid_point].horiz_center()) / 2    
    min_dist_strip = closest_pair_strip(cluster_list, mid_strip, min_dist[0])
    if min_dist_strip[0] < min_dist[0]:
        min_dist = min_dist_strip
    
    return min_dist


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """

    mid_clusters = []
    for index in range(len(cluster_list)):
        if abs(cluster_list[index].horiz_center() - horiz_center) < half_width:
            mid_clusters.append((cluster_list[index],index))
    
    num_of_mid_clusters = len(mid_clusters)
    
    mid_clusters.sort(key = lambda cluster: cluster[0].vert_center())
    min_dist = (float('inf'), -1, -1)    
    
    for index1 in range(num_of_mid_clusters -1):
        for index2 in range(index1 +1, min(index1 +3, num_of_mid_clusters)):            
            dist = pair_distance(cluster_list, mid_clusters[index1][1], mid_clusters[index2][1])          
            if dist[0] < min_dist[0]:
                min_dist = (dist[0], min(mid_clusters[index1][1], mid_clusters[index2][1]), max(mid_clusters[index1][1], mid_clusters[index2][1]))
    
    return min_dist
            
 
    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    return []


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    return []

