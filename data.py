
'''
all parameters we need to predefine before the iteration starts
'''
ant_num = None
alpha = None
beta = None
ant_bw = None
original_pheromone = None
# evaporate parameter for local update
rau = None
# evaporate parameter for global update
Delta = None

delta_tau = None

L_0 = None

'''
store the iteration result
they should be immutable once they are returned
'''
L_list = [L_0]
final_path_list = []
final_best_path_list = []
'''
data structure
'''
topoMatrix =[[]]
delay = [[]]
packet_loss = [[]]

local_node_state = {node:[pheromone, load]}
global_node_state = {node:[pheromone, max_load]}

