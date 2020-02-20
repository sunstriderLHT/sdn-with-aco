from path import Path


path_list = []
path_load_list = []
path_cost_list = []            

for i in range(len(path_list)):
    path = Path(path_list[i])
    path_load_list.append(path.load)
    path_cost_list.append(path.cost)


def select_best_path(path_load_list, path_cost_list, L):
    
    minimum = min(path_cost_list)
    path_load_cost = zip(path_load_list, path_cost_list)
    
    
    best_path_index = [i for i in range(len(path_load_cost)) \
        if path_load_cost[i][0] <= L and path_load_cost[i][1]== minimum]
    for index in best_path_index:
        pass
        