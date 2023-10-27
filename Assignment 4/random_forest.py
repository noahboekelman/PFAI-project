'''
random_forest.py

Author Korbinian Randl
'''
from decision_tree import BinaryDecisionTree
import random

def most_frequent(List):
    counter = 0
    num = List[0]
    
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num

class BinaryRandomForest:
    def __init__(self, X:dict, y:list, n_trees:int, bias:float=.5, max_depth:int=float('inf')) -> None:
        '''Creates and trains a binary random forest.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.

            n_trees:    number of trees in the forest.

            bias:       decision bias for non-pure leaves.

            max_depth:  max_depth of the tree.
        '''
        self.trees = [BinaryDecisionTree(*self.get_sample(X, y), **{'bias':bias, 'max_depth':max_depth}) for _ in range(n_trees)]

    def predict(self, X:dict) -> bool:
        '''Predict the class of the input.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

        
        returns:        predicted boolean class
        '''
        predictions = [tree.predict(X) for tree in self.trees]
        return most_frequent(predictions)

    def get_sample(self, X:dict, y:list) -> dict:
        '''Implements feature bagging for X.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.

            
        returns:        a bootstrap sample of X and y
        '''
        print(X.keys())
        indices = random.choices(range(len(y)), k=len(y))
        X_ = dict()
        for key in X.keys(): X_[key] = [X[key][i] for i in indices]
        y_ = [y[i] for i in indices]
        return X_, y_