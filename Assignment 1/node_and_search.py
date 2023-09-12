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
        self.deepest=0
    
    def statistics(self, depth, t1, t2, found=True):
            print('----------------------------')
            print(f"Elapsed time (s): {t2-t1}")
            if found: print(f"Solution found at depth: {depth}")
            else: print(f"No solution found until depth: {depth}")
            print(f"Number of nodes explored: {self.cost}")
            print(f"Estimated effective branching factor: {self.cost / depth}")
            print('----------------------------')
        
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
                if statistics: self.statistics(self.deepest, t1, process_time(), found=False)
                return None
            curr_node = frontier.get()
            self.cost+=1
            if curr_node.depth>self.deepest: self.deepest=curr_node.depth

            #Solution found
            if curr_node.goal_state():
                if statistics: self.statistics(curr_node.depth, t1, process_time(), found=True)
                stop = True
                return curr_node

            #If verbose
            if verbose: 
                print(f"Exploring node from {curr_node.action}:")
                curr_node.state.pretty_print()
                  
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
                    

    def dfs(self, verbose=False, statistics=False, max_depth=None, check_visited=True):
        frontier = queue.LifoQueue() #LIFO, so first we visit the most recently opened nodes
        frontier.put(self.start)
        stop=False
        if check_visited: visited=set()
        if verbose:
            print("DFS exploration:\nStarting node:")
            self.start.state.pretty_print()
        if statistics: t1=process_time()

        while not stop:
            if frontier.empty():
                if statistics: self.statistics(slef.deepest, t1, process_time(), found=False)
                return None
            curr_node=frontier.get()
            self.cost+=1
            if curr_node.depth>self.deepest: self.deepest=curr_node.depth

            #Goal state check
            if curr_node.goal_state():
                if statistics: self.statistics(curr_node.depth, t1, process_time(), found=True)
                stop=True
                return curr_node

            #Boring verbose 
            if verbose:
                print(f"Exploring node from {curr_node.action}:")
                curr_node.state.pretty_print()

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
        

    def ids(self, verbose=False, statistics=False, max_depth=None, check_visited=True):
        stop=True
        depLim=0
        if statistics: t1=process_time()
        while not stop:
            depLim+=1
            goal_state = self.dfs(verbose=False, statistics=False, max_depth=depLim, check_visited=check_visited)
            self.cost+=goal_state.cost
            if goal_state != None:
                if statistics: self.statistics(goal_state.state.depth, t1, process_time(), found=True)
                return goal_state
        
        if statistics: self.statistics(self.deepest, t1, process_time(), found=False)
        return None