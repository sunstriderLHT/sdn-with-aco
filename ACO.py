# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 16:32:53 2020

@author: 16132
"""
import random
import copy
import time
import sys
import math
import tkinter #//GUI模块
import threading
from functools import reduce
(ALPHA, BETA,ROU,Q) = (1.0,2.0,0.5,100.0)
nodes_list = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
(node_num,ant_num) = (len(nodes_list),50)

nodes_graph = [[0 for node in nodes_list] for node in nodes_list]
pheromone_graph = [[1.0 for node in nodes_list] for node in nodes_list]
status_graph = [[0.0 for node in nodes_list] for node in nodes_list]

class Ant(object):
    def __init__(self,ID,start_node,end_node):
        
        self.ID = ID
        self.init_ant()
        self.start_node = start_node#根据用户输入确定出生点
        self.end_node = end_node#根据用户输入确定目的地
        
    def __init_ant(self):
        
        self.path = []  #当前蚂蚁路径
        self.move_count = 0 #移动次数
        self.total_cost = 0 #路径消耗
        self.current_node = -1  #当前停留switch
        
        
        self.current_node = self.start_node #记录初始节点为当前节点
        self.path.append(self.current_node) #将当前节点记录到路径列表中
        self.move_count = 1 #移动次数记录为1
        
    def __choice_next_node(self):
        
        avail_node = get_next_available_node_list(self.current_node) #通过方法得到当前节点的可连接节点
        
        select_node_prob = [0.0 for i in avail_node] #初始化所有节点选择概率为 0.0
        
        total_prob = 0  #初始化总概率
        
        for i in range(node_num):
            if avail_node[i]:
                select_node_prob[i] = pow(pheromone_graph[self.current_city][i], ALPHA) * pow((1.0/status_graph[self.current_city][i]), BETA)  #如果是可连接节点则计算出其选择概率
                total_prob +=select_node_prob[i]  # 得到概率之和
        
        #轮盘选择node
        if total_prob > 0.0:
            #产生一个随机概率
            temp_prob = random.uniform(0.0, total_prob)
            for i in range(node_num):
                if avail_node[i]: #如果是可连接节点
                    temp_prob -= select_node_prob[i]    #轮次相减至小于0时退出循环
                    if temp_prob < 0.0:
                        next_node = i
                        break
        
        return next_node
    
    def path_cost(self):
        temp_cost = 0
        
        for i in range(1,len(self.path)):
            start, end = self.path[i], self.path[i-1]
            temp_cost += status_graph[start][end]
        self.total_cost = temp_cost    
        
    def __move(self, next_node):
        
        self.path.append(next_node)
        self.current_node = next_node
        self.move_count += 1 
    
    def search_path(self):

        self.__clean_data()
        
        while self.current_node != self.end_node:
        
            next_node = self.__choice_next_node()
            self.__move(next_node)
        
        self.path_cost()
                
#--------------------------------------------------------------------------                
                    
def get_next_available_node_list(node):# 用True 或是False表示是否与当前节点连接
    return list


#-------------------------------------------------------------------
    
class Find_Best_Path(object):
    
    def new(self,start_node,end_node):
        
        for i in range(node_num):
            for j in range(node_num):
                pheromone_graph[i][j] = 1.0
        
        self.ants = [Ant(ID,start_node,end_node) for ID in range(ant_num)]
        self.best_ant = Ant(-1) #初始化最优解
        self.iter = 1
    

    def search_path(self):
        
        while self.__running:
            
            for ant in self.ants:
                
                ant.search_path()
                
                if ant.total_cost < self.best_ant.total_distance:
                    
                    self.best_ant = copy.deepcopy(ant)
                
            self.__update_pheromone_graph()
            
    def __update_pheromone_graph(self):
        
        temp_pheromone = [[0.0 for node in range(node_num)] for node in range(node_num)]
        
        for ant in self.ants:
            for i in range(1,len(ant.path)):
                start, end = ant.path[i-1], ant.path[i]
                
                temp_pheromone[start][end] += Q / ant.total_cost
        
        for i in range(node_num):
            for j in range(node_num):
                pheromone_graph[i][j] = pheromone_graph[i][j] *ROU + temp_pheromone[i][j]

























