
from ant import Ant
from functionalities import check_reachability
from data import local_node_state, ant_bw, delay

class Path:
    def __init__(self, path):
        self.path = path
        self.load = None
        self.cost = None

    def load(self):
        load_list = []
        for node in self.path:
            load = local_node_state[node][1] * ant_bw
            load_list.append(load)
        load = max(load_list)
        self.load = load

    def cost(self):
        total_cost = 0 
        for i in range(len(self.path) - 1):
            total_cost += delay[self.path[i]][self.path[i+1]]
        self.cost = total_cost

# the method for one ant to find its path
def find_path(start_node, end_node):

    ant = Ant(start_node, end_node)

    while ant.current_node != ant.end_node:
        # append its current node to its path
        ant.construct_path()
        # update the state of its current node
        ant.update_node_state()
        # choose the next node from available nodes
        available_nodes = check_reachability(ant.current_node, ant.end_node)
        next_node = ant.choose_next_node(available_nodes)
        # move to the next node
        ant.move(next_node)

    return ant.path


def calculate_load_cost(path_list):
    path_load_list = []
    path_cost_list = []
    for i in range(len(path_list)):
        path = Path(path_list[i])
        path_load_list.append(path.load())
        path_cost_list.append(path.cost())

    return [path_load_list, path_cost_list]

def select_best_path(path_load_list, path_cost_list, L):
    minimum = min(path_cost_list)
    path_load_cost = zip(path_load_list, path_cost_list)

    best_path_index = [path_load_list.index(cost) for load, cost in path_load_cost \
                       if load <= L and cost == minimum]

    return best_path_index
    
            
            
        