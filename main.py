from path import find_path, calculate_load_cost, select_best_path
from functionalities import predict_next_L, reset_local_node_state, global_update_state

from data import L_list, final_path_list, final_best_path_list
from data import local_node_state, ant_num

count = 0
path_list = []

# each ant completes the search process, count++
# until all ants complete this job
while count != ant_num:
    path = find_path(1, 8)
    path_list.append(path)
    count += 1

# store the path_list of the m-th iteration in final_path_list
# final_path_list[i] indicates the path_list of the i-th iteration
final_path_list.append(path_list)

# calculate the threshold of the iteration based on path_list
# append the threshold to the result list
# L_list[i] indicates the threshold of the i-th iteration
path_load_list, path_cost_list = calculate_load_cost(path_list)
L = predict_next_L(path_load_list)
L_list.append(L)

# get the best path for one iteration
# store it in final_best_path_list
# final_best_path[i] indicates the best path of the i-th iteration
best_path = [path_list[i] for i in select_best_path(path_load_list, path_cost_list, L_list[-1])]
final_best_path_list.append(best_path)

# reset local state as the original level after completing one iteration
# then update global_node_state
reset_local_node_state(local_node_state)
global_update_state(final_path_list[-1], final_best_path_list[-1])





