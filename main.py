from path import find_path, calculate_load_cost, select_best_path
from functionalities import predict_next_L, reset_local_node_state, global_update_state

from data import L_list
from data import local_node_state
from data import store_global_node_state, store_iteration_result

import sys


def main(ant_num, iteration):
    count = 0
    path_list = []

    # each ant completes the search process, count++
    # until all ants complete this job
    while count != ant_num:
        path = find_path(0, 6)
        # print('***', path)
        path_list.append(path)
        count += 1

    # store the path_list of the m-th iteration in final_path_list
    # final_path_list[i] indicates the path_list of the i-th iteration
    store_iteration_result('path.xlsx', path_list, iteration)

    # calculate the threshold of the iteration based on path_list
    # append the threshold to the result list
    # L_list[i] indicates the threshold of the i-th iteration
    path_load_list, path_cost_list = calculate_load_cost(path_list)
    # print(path_cost_list)
    L = predict_next_L(path_load_list)
    L_list.append([L])
    print(L_list)
    store_iteration_result('l.xlsx', L_list, iteration)

    # get the best path for one iteration
    # store it in final_best_path_list
    # final_best_path[i] indicates the best path of the i-th iteration
    best_path = [path_list[i] for i in select_best_path(path_load_list, path_cost_list, L_list[-1])]
    store_iteration_result('bestPath.xlsx', best_path, iteration)

    # print(best_path)
    # reset local state as the original level after completing one iteration
    # then update global_node_state
    reset_local_node_state(local_node_state)

    # except the first iteration, each iteration get_global_node_state
    # from 'globalNodeState{iteration - 1}.xlsx'
    # namely, get the node state from the last iteration result
    global_node_state = global_update_state(path_list, best_path)

    store_global_node_state('globalNodeState.xlsx', global_node_state, iteration)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ant_num = sys.argv[1]
        # sys.argv returns 'String', must convert into 'number'
        iteration = 1
        while True:
            main(int(ant_num), iteration)
            confirm = input('Do you want to iteration again? y/n')
            if confirm == 'y':
                iteration += 1
                continue
            else:
                print(f'You have iterated {iteration} times!')
                break
    else:
        raise('you only can provide 1 parameter \ '
              'as the number of ants for the iteration!')



