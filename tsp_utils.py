import math
import random
import numpy as np


def vectorToDistMatrix(coords):
    '''
    Create the distance matrix
    '''
    xCoords = coords[:, [0, 1]]
    zCoords = coords[:, [2,3]]
    penaltyMarCortez = 1
    penaltyGolfo = 10
    dist = np.sqrt((np.square(xCoords[:, np.newaxis] - xCoords).sum(axis=2)) + penaltyGolfo * np.square(zCoords[:, np.newaxis] - zCoords).sum(axis=2))
    print(dist)
    return dist


def nearestNeighbourSolution(dist_matrix):
    '''
    Computes the initial solution (nearest neighbour strategy)
    '''
    node = random.randrange(len(dist_matrix))
    result = [node]

    nodes_to_visit = list(range(len(dist_matrix)))
    nodes_to_visit.remove(node)

    while nodes_to_visit:
        nearest_node = min([(dist_matrix[node][j], j) for j in nodes_to_visit], key=lambda x: x[0])
        node = nearest_node[1]
        nodes_to_visit.remove(node)
        result.append(node)

    return result
