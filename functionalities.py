import numpy

import data

ant_bw = None
L = None
rau = None
Delta = None
delta_tau = None

def check_reachability(current_node, destination_node):
    
    available_nodes = []
    
    row = data.topoMatrix[current_node]
    nodes = [i for i, value in enumerate(row) if value == 1]
    
    for node in nodes:
        if node == destination_node:
            available_nodes.append(node)
        else:
            temp = data.topoMatrix[node]
            if sum(temp) > 1:
                available_nodes.append(node)
                
    return available_nodes

def calculate_probability(available_nodes, alpha, beta):
    
    influence_weight = []
    total_weight = 0
    
    for node in available_nodes:
        weight = data.local_node_state[node][0] ** alpha * (L - data.local_node_state[node][1] * ant_bw) ** beta
        total_weight += weight
        influence_weight.append(weight)
    
    probability_list = [influence_weight[i] / total_weight for i in range(len(influence_weight))]
    
    return probability_list


def local_update_state(node):
    data.local_node_state[node][0] *= (1-rau) + delta_tau
    data.local_node_state[node][1] += 1    

def global_update_state(node):
    data.gloal_node_state[node][0] *= (1-Delta) + delta_tau


def predict_next_L(path_load_list):
    average = numpy.mean(path_load_list)
    standard_deviation = numpy.std(path_load_list)
    
    L_next = average + standard_deviation
    
    return L_next