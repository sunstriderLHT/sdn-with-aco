import numpy

import data
from data import rau, Delta, delta_tau, ant_bw, original_pheromone


def check_reachability(current_node, destination_node):
    
    available_nodes = []

    # choose those nodes connected with current_node
    row = data.topoMatrix[current_node]
    nodes = [i for i, value in enumerate(row) if value == 1]
    
    for node in nodes:
        if node == destination_node:
            available_nodes.append(node)
        else:
            temp = data.topoMatrix[node]
            # make sure candidate nodes are connected with other nodes except current_node
            if sum(temp) > 1:
                available_nodes.append(node)
                
    return available_nodes

def calculate_probability(available_nodes, alpha, beta, L):
    
    influence_weight = []
    total_weight = 0
    
    for node in available_nodes:
        weight = data.local_node_state[node][0] ** alpha * (L - data.local_node_state[node][1] * ant_bw) ** beta
        total_weight += weight
        influence_weight.append(weight)
    
    probability_list = [weight / total_weight for weight in influence_weight]
    
    return probability_list

def local_update_state(node):
    data.local_node_state[node][0] *= (1-rau) + delta_tau
    data.local_node_state[node][1] += 1    

def reset_local_node_state(local_node_state):

    for node in local_node_state.keys():
        # all nodes are set with the original pheromone
        node[0] = original_pheromone
        # load of all nodes are back to the maximum level
        node[1] = data.global_node_state[node][1]

def global_update_state(path_list, best_path):

    for path in path_list:
        # we should add more pheromone for nodes on best_path
        if path not in best_path:
            for node in path:
                data.global_node_state[node][0] *= (1-Delta) + delta_tau
        else:
            for node in path:
                data.global_node_state[node][0] *= (1-Delta) + 2 * delta_tau


def predict_next_L(path_load_list):

    average = numpy.mean(path_load_list)
    standard_deviation = numpy.std(path_load_list)

    L_next = average + standard_deviation
    
    return L_next