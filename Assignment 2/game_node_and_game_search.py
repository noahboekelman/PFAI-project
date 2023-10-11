'''
Definitions for GameNode, GameSearch and MCTS

Author: Tony Lindgren
'''
from time import process_time
import random
import math


class GameNode:
    '''
    This class defines game nodes in game search trees. It keep track of: 
    state
    '''
    def __init__(self, state, node=None):
        self.state = state   
           
class GameSearch:
    '''
    Class containing different game search algorithms, call it with a defined game/node
    '''                 
    def __init__(self, game, depth=3):
        self.state = game       
        self.depth = depth

    def mcts(self):                     
        start_time = process_time() 
        tree = GameNode(self.state)
        tree.actions_left = tree.state.actions()   
        elapsed_time = 0
        while elapsed_time < self.time:   
            leaf = self.select(tree)
            child = self.expand(leaf)               
            result = self.simulate(child) 
            self.back_propagate(result, child)         
            stop_time = process_time()
            elapsed_time = stop_time - start_time
        move = self.actions(tree)
        return move
    
    def minimax_search(self, ab=False, timeLimit=None): 
        self.start_time = process_time()
        if (ab): 
            self.alpha = -100000
            self.beta = 100000
        _, move = self.max_value(self.state, self.depth, ab)  
        return move
    
    def max_value(self, state, depth, ab=False, timeLimit=None):
        move = None
        terminal, value = state.is_terminal()
        if terminal:
            return value, None
        elif depth == 0 or (timeLimit != None and timeLimit < process_time() - self.start_time):
            return state.evaluate(), None
        v = -100000
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.min_value(new_state, depth - 1)
            if v2 > v:
                v = v2
                move = action
                self.alpha = max(self.alpha, v)
            if v >= self.beta:
                return v, move
        return v, move
    
    def min_value(self, state, depth, ab=False, timeLimit=None):
        move = None
        terminal, value = state.is_terminal()
        if terminal:
            return value, None  
        elif depth ==0 or (timeLimit != None and timeLimit < process_time() - self.start_time):
            return state.evaluate(), None
        v = 100000
        actions = state.actions()
        for action in actions: 
            new_state = state.result(action)
            v2, _ = self.max_value(new_state, depth - 1)
            if v2 < v:
                v = v2
                move = action
                self.beta = min(self.beta, v)
            if v <= self.alpha:
                return v, move
        return v, move
