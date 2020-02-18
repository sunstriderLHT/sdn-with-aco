import math
import numpy
# store the ppheromone of each node in the dictionary
# L_0 should be the maximum bandwidth of each link
alpha = 1
beta = 1
theta = 1
pheromone_value = None
delta_tau = None
L_0 = None

max_link_load = None
tau_predefined = None

global_node_state = {
    node: [float(pheromone_value), float(max_link_load)]
}

# global_update_pheromone will not change the state of link load
def global_update_pheromone(path_list, best_path_nodes, rau):
    
    for node in global_node_state.keys():
        global_node_state[node][0] = tau_predefined
        # update the phermone of those nodes in path_list
        if node in path_list:
            global_node_state[node][0] *= (1-rau) + rau * delta_tau
        # update the pheromone of those nodes on best_path
        if node in best_path_nodes:
            global_node_state[node][0] += rau * delta_tau
        
    return global_node_state

local_pheromone_value = None
link_load = None

local_node_state = {
    node: [float(local_pheromone_value), float(link_load)]
}

# local_update_state wil change the two values of pheromone and link load
def local_update_state(node_i, k, L, Delta):
    # before node_i is visited by the next ant, local_update_pheromone must be completed
    local_node_state[node_i][0] *= (1-Delta) + Delta * delta_tau
    # update the avaiable bandwidth of node_i
    local_node_state[node_i][1] = L - k * delta_tau 
    
    return local_node_state
        
# how to abstract nodes from path_list

topologyMatrix = [[]]
n = len(topologyMatrix)

# current_node should be a list of its coordinates in the topologyMatrix
def check_reachability(current_node_coordinates):
    row_index = current_node_coordinates[0]
    col_index = current_node_coordinates[1]
    # store all candidate nodes 
    available_nodes = []
    
    for i in range(n - row_index):
        if topologyMatrix[row_index + i][col_index] == 1:
            for j in range(col_index, n + 1):
                if topologyMatrix[row_index + i][j] == 1:
                    available_nodes.append(row_index + i)
                    
    return available_nodes

def calculate_proability(available_nodes):
    proability_list = []
    weight_list = []
    
    for node in available_nodes:
        node_tau = local_node_state[node][0]
        node_load = local_node_state[node][1]
        interest_weight = node_tau ** alpha * node_load ** beta
        weight_list.append([node, interest_weight])
    for i in range(len(weight_list)):
        bottom = sum(weight_list[i][1])
        p = weight_list[i][1] / bottom
        proability_list.append([weight_list[i][0], p])
    
    return proability_list
    
def max_node_proability(proability_list):
    maximum = proability_list[0]
    
    for item in proability_list:
        if item[1] > maximum[1]:
            maximum = item
    return maximum 
   
def construct_path(current_node, path = []):
     path.append(current_node)
     return path

def construct_path_list(path, path_list = []):
    path_list.append(path)
    return path_list
    
def choose_next_node(current_node):
    available_nodes = check_reachability(current_node)
    proability_list = calculate_proability(available_nodes)
    next_node = max_node_proability(proability_list)[0]
    return next_node

def calculate_load(path, L = L_0):
    load_list = []
    for i in range(len(path)):
        load = L - local_node_state[path[i]][1]
        load_list.append(load)
    path_load = max(load_list)
    return path_load
        
def predict_next_L(path_list):
    load_path = []
    for path in path_list:
        path_load = calculate_load(path)
        load_path.append(path_load)
    
    average = sum(load_path) / len(load_path)
    variance_list = []
    
    for load in load_path:
        variance_list.append((load - average) ** 2)
    standardDeviation = math.sqrt(sum(variance_list) / len(variance_list))
    
    L_next = average + standardDeviation

    return L_next

# delay[i][j] can be set based on topologyMatrix
delay = [[]]
# packet_loss[i][j] can also be set based on topologyMatrix
packet_loss = [[]]

def cost(i, j):
    cost = (1-theta) * delay[i][j] + theta * packet_loss[i][j]
    return cost

def select_best_path(path_list):
    cost_list = []
    for path in path_list:
        cost_path = 0
        for i in range(len(path) - 1):
            cost_path += cost(path[i], path[i+1])
        cost_list.append([path_list.index(path), cost_path])
    
    
            
        
    

    

    
    
    
    

