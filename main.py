from path import find_path, calculate_load_cost, select_best_path
from functionalities import reset_local_node_state, global_update_state

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
        path_list.append(path)
        count += 1

    # store the path_list of the m-th iteration in final_path_list
    # final_path_list[i] indicates the path_list of the i-th iteration
    store_iteration_result('path.xlsx', path_list, iteration)

    # calculate the threshold of the iteration based on path_list
    # append the threshold to the result list
    # L_list[i] indicates the threshold of the i-th iteration
    path_load_list, path_cost_list = calculate_load_cost(path_list)
    print('****', path_load_list)
    print('####', path_cost_list)
    # get the best path for one iteration
    best_path = [path_list[i] for i in select_best_path(path_cost_list)]
    best_path_load = [[path_load_list[i]] for i in select_best_path(path_cost_list)]
    store_iteration_result('bestPath.xlsx', best_path, iteration)
    store_iteration_result('bestPathLoad.xlsx', best_path_load, iteration)

    # reset local state as the original level after completing one iteration
    # then update global_node_state
    reset_local_node_state(local_node_state)

    global_node_state = global_update_state(path_list, best_path)
    store_global_node_state('globalNodeState.xlsx', global_node_state, iteration)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        ant_num = sys.argv[1]
        # sys.argv returns 'String', must convert into 'number'
        iteration = 1
        while True:
            main(int(ant_num), iteration)
            confirm = input('Do you want to iteration again? (y/n)\n')
            if confirm == 'y':
                ant_num = input('please enter the new ant_num:\n')
                iteration += 1
                continue
            else:
                print(f'You have iterated {iteration} times!')
                break
    else:
        raise('you only can provide 1 parameter \ '
              'as the number of ants for the iteration!')



