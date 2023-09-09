'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue

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
        print(f"action: {self.action}")
        self.parent.pretty_print_solution(verbose)
        
             
class SearchAlgorithm:
    '''
    Class for search algorithms, call it with a defined problem 
    '''
    def __init__(self, problem):
        self.start = Node(problem)        
        
    def bfs(self):
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        visited = set()
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            curr_node.state.deb()
            if curr_node.goal_state():
                stop = True    
                return curr_node    


            if (curr_node.state.state_val() in visited and curr_node.depth >= 1): #BFS: depth when visited doesn't matter, will always be the shortest.
                print(visited)
                continue

            visited.add(curr_node.state.state_val())

            successor = curr_node.successor() 
            while not successor.empty():
                frontier.put(successor.get())
                    