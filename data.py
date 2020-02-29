import xlrd

'''
all parameters we need to predefine before the iteration starts
'''
ant_num = 20
ant_bw = 1

alpha = 2
beta = 1
original_pheromone = 1
# evaporate parameter for local update
rau = 0.3
# evaporate parameter for global update
Delta = 0.2

# small as much as possible
delta_tau = 0.3

# the maximum bandwidth of all links
L_0 = 25

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
def get_matrix(path):
    matrix = []
    x_workbook = xlrd.open_workbook(path)
    sheet = x_workbook.sheets()[0]
    rows = sheet.nrows
    for row in range(rows):
        matrix.append(sheet.row_values(row))

    return matrix

topoMatrix = get_matrix('topoMatrix.xlsx')
delay = get_matrix('delay.xlsx')

max_load = [20, 20, 25, 25, 25, 20, 25, 25, 20, 25]
local_node_state = {i:[original_pheromone, 0] for i in range(10)}
global_node_state = {i:[original_pheromone, max_load[i]] for i in range(10)}


