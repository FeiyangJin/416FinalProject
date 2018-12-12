import numpy
import networkx as nx
import operator
import timeit
from numpy import linalg as LA


def  betweennessBasedClustering (G,k):
    n = nx.number_connected_components(G)
    numE = G.number_of_edges()
    # check how many clusters we have right now
    while n < k:
        #compute betweenness
        e = nx.edge_betweenness_centrality(G)
        se = sorted(e.items(), key=operator.itemgetter(1))
        #remove the edge with largest betweenness
        currentEdge = se[-1][0]
        G.remove_edge(*currentEdge)
        n = nx.number_connected_components(G)
    return nx.connected_component_subgraphs(G)
    #print modularity(G, nx.connected_components(G), numE)

def modularityMaximization(G, k):
    n = nx.number_connected_components(G)
    numE = G.number_of_edges()
    # check how many clusters we have right now
    while n < k:
        flag = True
        # build matrix a and b
        for subgraph in nx.connected_component_subgraphs(G):
            matrixA =nx.adj_matrix(subgraph).toarray().astype(float)
            matrixB = matrixA
            nodes = list(subgraph.nodes())
            l = len(nodes)
            for i in range(0, l):
                for j in  range(0, l):
                    matrixB[i,j]= matrixA[i,j]-subgraph.degree(nodes[i])*subgraph.degree(nodes[j])/(numE*2.0)
            (value, vector) = LA.eig(matrixB)
            maxVector = vector[:, numpy.argmax(value)]
            #remove the edges with two nodes that have different eigenvalues
            for (parent, child) in nx.edges(subgraph):
                if maxVector[nodes.index(parent)]*maxVector[nodes.index(child)] < 0:
                    G.remove_edge(parent,child)
                    flag = False
        if flag:
            break
        n = nx.number_connected_components(G)
    return nx.connected_component_subgraphs(G)