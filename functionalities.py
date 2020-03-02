import numpy

import data
from data import rau, Delta, delta_tau, ant_bw, original_pheromone, max_load

def check_reachability(previous_node, current_node, destination_node):
    
    available_nodes = []

    # choose those nodes connected with current_node
    row = data.topoMatrix[current_node]
    nodes = [i for i, value in enumerate(row) if value == 1]
    
    for node in nodes:
        if node == destination_node:
            available_nodes.append(node)
        elif node != previous_node:
            temp = data.topoMatrix[node]
            # make sure candidate nodes are connected with other nodes except current_node
            if sum(temp) > 1:
                available_nodes.append(node)

    return available_nodes

def calculate_probability(available_nodes, alpha, beta):
    influence_weight = []
    total_weight = 0
    
    for node in available_nodes:
        if data.local_node_state[node][1] < max_load[node]:
            weight = data.local_node_state[node][0] ** alpha * (max_load[node] - data.local_node_state[node][1] * ant_bw) ** beta
        else:
            # when available load is exhausted
            # no ant chooses the node
            weight = 0
        total_weight += weight
        influence_weight.append(weight)

    # print(total_weight, ':', influence_weight)
    try:
        probability_list = [weight / total_weight for weight in influence_weight]
    except ZeroDivisionError:
        raise('the network has been the maximum level! More traffic must be in queuing!')
    
    return probability_list

def local_update_state(node):
    data.local_node_state[node][0] *= (1-rau) + delta_tau
    data.local_node_state[node][1] += 1    

def reset_local_node_state(local_node_state):

    for node in local_node_state:
        # all nodes are set with the original pheromone
        node[0] = original_pheromone
        # load of all nodes are back to the maximum level
        node[1] = 0

def global_update_state(path_list, best_path):
    global_node_state = data.global_node_state[:]
    for path in path_list:
        # we should add more pheromone for nodes on best_path
        if path not in best_path:
            for node in path[1:]:
                global_node_state[node][0] *= (1-Delta) + delta_tau
        else:
            for node in path[1:]:
                global_node_state[node][0] *= (1-Delta) + 2 * delta_tau
    return global_node_state

# def predict_next_L(path_load_list):
#
#     average = numpy.mean(path_load_list)
#     standard_deviation = numpy.std(path_load_list)
#
#     L_next = average - standard_deviation
#
#     if L_next > max(max_load):
#         return max(max_load)
#     else:
#         return L_next