import random

import functionalities

alpha = None
beta = None
ant_bw = None
class Ant:
    
    def __init__(self, start_node, end_node, ant_bw):
        self.start_node = start_node
        self.end_node = end_node
        self.path = []
        self.current_node = start_node
        
    def choose_next_node(self, available_nodes):
        
        probability_list = functionalities.calculate_probability(available_nodes, alpha, beta)
        max_probability = max(probability_list)
        
        max_node = [i for i, p in enumerate(probability_list) if p == max_probability]
        
        anchor = random.randint(0, len(max_node)- 1)
        next_node = available_nodes[max_node[anchor]]
            
        return next_node
    
    def update_node_state(self):
        functionalities.local_update_state(self.current_node)
    
    def construct_path(self):
        self.path.append(self.current_node)
        
    def move(self, next_node):
        self.current_node = next_node
        
    
        