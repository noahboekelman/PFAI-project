'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
from collections import deque
from time import process_time
from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

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
        
    def score(self, heuristic, a_star):
        return self.state.score(heuristic) + self.cost*a_star
             
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
            print(f"Elapsed time (s): {t2-t1 :.2f}")
            if found: print(f"Solution found at depth: {depth}")
            else: print(f"No solution found until depth: {depth}")
            print(f"Number of nodes explored: {self.cost}")
            print(f"Estimated effective branching factor: {self.cost / depth :.2f}")
            print('----------------------------')
        
    def bfs(self, verbose=False, statistics=False, check_visited=True, depth_limit=None):
        frontier = queue.Queue() #Queue, so least recently opened node is explored first
        frontier.put(self.start)
        stop = False
        self.cost=0
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
                visited.add(curr_node.state.state_val())

            #Generation of successors
            if depth_limit==None or curr_node.depth < depth_limit:
                successor = curr_node.successor() 
                while not successor.empty():
                    nextSuccessor=successor.get()
                    if check_visited and nextSuccessor.state.state_val() in visited: continue
                    else: frontier.put(nextSuccessor)
                    

    def dfs(self, verbose=False, statistics=False, depth_limit=None, check_visited=True, independent=True):
        frontier = queue.LifoQueue() #LIFO, so first we visit the most recently opened nodes
        frontier.put(self.start)
        stop=False
        if independent: self.cost=0
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
                visited.add(curr_node.state.state_val())
            
            #Successors generation
            if depth_limit==None or curr_node.depth < depth_limit:
                successor=curr_node.successor()
                while not successor.empty():
                    nextSuccessor=successor.get()
                    if check_visited and nextSuccessor.state.state_val() in visited: continue
                    frontier.put(nextSuccessor)
        

    def ids(self, verbose=False, statistics=False, depth_limit=None, check_visited=True):
        stop=False
        depLim=0
        self.cost=0
        if statistics: t1=process_time()
        while not stop and (depth_limit == None or depLim<depth_limit):
            depLim+=1
            solution = self.dfs(verbose=False, statistics=False, depth_limit=depLim, check_visited=check_visited, independent=False)
            if solution != None:
                if statistics: self.statistics(solution.depth, t1, process_time(), found=True)
                return solution
        
        if statistics: self.statistics(self.deepest, t1, process_time(), found=False)
        return None

    def greedy_search(self, heuristic=0, depth_limit=None, verbose=False, statistics=False, check_visited=True, a_star=False):
        frontier=queue.PriorityQueue()
        frontier.put(PrioritizedItem(0, self.start))
        Stop=False
        self.cost=0
        if check_visited: visited=dict()
        if verbose:
            print("Starting search")
        if statistics: t1=process_time()

        while not Stop:
            if frontier.empty():
                print("Search ended, goal not found.")
                if statistics: self.statistics(self.deepest, t1, process_time(), found=False)
                return None
            curr_node=frontier.get().item
            self.cost+=1
            if curr_node.depth>self.deepest:self.deepest=curr_node.depth

            if verbose:
                print("Current frontier:")
                curr_node.state.pretty_print()

            if curr_node.goal_state():
                if verbose: print("Goal found!")
                if statistics: self.statistics(curr_node.depth, t1, process_time(), found=True)
                stop=True
                return curr_node

            #Store the state and the depth at which it was encountered
            if check_visited:
                visited[curr_node.state.state_val()]=curr_node.depth 
                

            if depth_limit==None or curr_node.depth < depth_limit:
                successor=curr_node.successor()
                while not successor.empty():
                    nextSuccessor=successor.get()
                    if check_visited:
                        #We skip the successor only if it was explored on a higher layer
                        #That way, we only explore already explored states if we found a shorter way to go to them.
                        if nextSuccessor.state.state_val() in visited.keys(): 
                            if visited[nextSuccessor.state.state_val()]<=nextSuccessor.depth:
                                continue
                    frontier.put(PrioritizedItem(nextSuccessor.score(heuristic, a_star), nextSuccessor))
