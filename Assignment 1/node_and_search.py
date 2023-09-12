'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
from collections import deque
from time import process_time

class Node:
    '''
    This class defines nodes in search trees. It keep track of: 
    state, cost, parent, action, and depth 
    '''
    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1 

    def goal_state(self):
        return self.state.check_goal()
    
    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:                     
            child = self.state.move(action)      
            if child != None:                                
                childNode = Node(child, self.cost + 1, self, action)              
                successors.put(childNode)
        return successors  
    
    def pretty_print_solution(self, verbose=False):
        if self.action == None:
            return
        self.parent.pretty_print_solution(verbose)
        print(f"action: {self.action}")
        if verbose:
            self.state.pretty_print()
        
             
class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''
    def __init__(self, problem):
        self.start = Node(problem)      
        self.cost=0  
        
    def bfs(self, verbose=False, statistics=False, check_visited=True):
        frontier = queue.Queue() #Queue, so least recently opened node is explored first
        frontier.put(self.start)
        stop = False
        if check_visited: visited = set()
        if verbose:
            print("BFS Exploration:\nStart node:")
            self.start.state.pretty_print()
        if statistics: t1 = process_time()

        #Start exploration
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            self.cost+=1

            #Solution found
            if curr_node.goal_state():
                stop = True
                continue

            #If verbose
            if verbose: 
                print(f"Exploring node from {curr_node.action}:")
                curr_node.pretty_print()
                  
            #Elimination of explored nodes
            if check_visited:
                if (curr_node.state.state_val() in visited): #BFS: depth when visited doesn't matter, will always be the shortest.
                    if verbose: print("Node already explored, skipping successors...")
                    continue
                visited.add(curr_node.state.state_val())

            #Generation of successors
            successor = curr_node.successor() 
            while not successor.empty():
                frontier.put(successor.get())

        #Statistics
        if statistics: 
            t2 = process_time()   
            print('----------------------------')
            print(f"Elapsed time (s): {t2-t1}")
            print(f"Solution found at depth: {curr_node.depth}")
            print(f"Number of nodes explored: {self.cost}")
            print(f"Estimated effective branching factor: {self.cost / curr_node.depth}")
            print('----------------------------')
        return curr_node  
                    

    def dfs(self, verbose=False, statistics=False, max_depth=None, check_visited=True):
        frontier = queue.LifoQueue() #LIFO, so first we visit the most recently opened nodes
        frontier.put(self.start)
        stop=False
        if check_visited: visited=set()
        if verbose:
            print("DFS exploration:\nStarting node:")
            self.state.pretty_print()
        if statistics: t1=process_time()

        while not stop:
            if frontier.empty():
                return None
            curr_node=frontier.get()
            self.cost+=1

            #Goal state check
            if curr_node.goal_state():
                stop=True
                continue

            #Boring verbose 
            if verbose:
                print(f"Exploring node from {curr_node.action}:")
                curr_node.pretty_print()

            #Already visited check
            if check_visited:
                if (curr_node.state.state_val() in visited):
                    continue
                visited.add(curr_node.state.state_val())
            
            #Successors generation
            if curr_node.depth < max_depth:
                successor=curr_node.successor()
                while not successor.empty():
                    frontier.put(successor.get())

        #Statistics
        if statistics: 
            t2 = process_time()   
            print('----------------------------')
            print(f"Elapsed time (s): {t2-t1}")
            print(f"Solution found at depth: {curr_node.depth}")
            print(f"Number of nodes explored: {self.cost}")
            print(f"Estimated effective branching factor: {self.cost / curr_node.depth}")
            print('----------------------------')
        return curr_node  
        
    def idfs(self, verbose=False, statistics=False, max_depth=None, check_visited=True):
        frontier=queue.LifoQueue()
        return None