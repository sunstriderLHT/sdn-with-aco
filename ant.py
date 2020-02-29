import random
from functionalities import calculate_probability, local_update_state
from data import alpha, beta, L_list

class Ant:
    '''
    each ant is only responsible for four functions:
    @choose_next_node: decide he next node it should move
    @update_node_state: update the state of its current node
    @construct_path: add its current_node to its path
    @move: set next_node as its current_node

    when initialising one ant, we just need to set start_node and end_node
    '''

    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.path = []
        self.current_node = start_node
        self.previous_node = None
        
    def choose_next_node(self, available_nodes):
        '''
        first check whether end_node is in available_nodes
        if exists, directly set end_node as next_node
        if not, choose the next_node according to the state of available nodes
        '''
        if self.end_node in available_nodes:
            next_node = self.end_node
        else:
            probability_list = calculate_probability(available_nodes, alpha, beta, L_list[-1])
            max_probability = max(probability_list)
            max_node_index = [i for i, p in enumerate(probability_list) if p == max_probability]
            anchor = random.randint(0, len(max_node_index)- 1)

            next_node = available_nodes[max_node_index[anchor]]
            
        return next_node
    
    def update_node_state(self):
        local_update_state(self.current_node)
    
    def construct_path(self):
        self.path.append(self.current_node)
        
    def move(self, next_node):
        self.previous_node, self.current_node = self.current_node, next_node
        
    
        