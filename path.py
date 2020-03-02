import numpy
from ant import Ant
from functionalities import check_reachability
from data import local_node_state, ant_bw, delay, max_load

class Path:
    def __init__(self, path):
        self.path = path

    # def load(self):
    #
    #     load_list = []
    #     for node in self.path:
    #         load = local_node_state[node][1] * ant_bw
    #         load_list.append(load)
    #     load = max(load_list)
    #     return load

    def global_load(self, max_load):
        load_list = [max_load[node] for node in self.path]
        global_load = min(load_list)
        return global_load

    def cost(self):
        total_cost = 0 
        for i in range(len(self.path) - 1):
            total_cost += delay[self.path[i]][self.path[i+1]]
        return total_cost

# the method for one ant to find its path
def find_path(start_node, end_node):

    ant = Ant(start_node, end_node)

    while ant.current_node != ant.end_node:
        # append its current node to its path
        ant.construct_path()
        # update the state of its current node
        ant.update_node_state()
        # choose the next node from available nodes
        available_nodes = check_reachability(ant.previous_node, ant.current_node, ant.end_node)
        next_node = ant.choose_next_node(available_nodes)
        # move to the next node
        ant.move(next_node)
    else:
        ant.path.append(ant.current_node)

    return ant.path


def calculate_load_cost(path_list):
    path_load_list = []
    path_cost_list = []
    for i in range(len(path_list)):
        path = Path(path_list[i])
        path_load_list.append(path.global_load(max_load))
        path_cost_list.append(path.cost())

    return [path_load_list, path_cost_list]

def select_best_path(path_cost_list):

    def sortSecond(val):
        return val[1]

    average_cost = numpy.mean(path_cost_list)
    temp = [i for i in enumerate(path_cost_list)]
    temp.sort(key=sortSecond)

    best_path_index = [cost[0] for cost in temp if cost[1] <= average_cost]

    return best_path_index

            
        