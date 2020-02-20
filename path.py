
from ant import ant_bw
import data

class Path:
    def __init__(self, path):
        self.path = path
    
    @property
    def load(self):
        load_list = []
        for node in self.path:
            load = data.local_node_state[node][1] * ant_bw
            load_list.append(load)
        load = max(load_list)
        self.load = load
        
        return self.load
    
    @property
    def cost(self):
        total_cost = 0 
        for i in range(len(self.path) - 1):
            total_cost += data.delay[self.path[i]][self.path[i+1]]
        self.cost = total_cost
        
        return self.cost
 


    
    
    
            
            
        