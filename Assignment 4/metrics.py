'''
metrics.py

Author Korbinian Randl
'''

def get_false_positives(y_true:list, y_pred:list) -> int:
    '''Returns the number of false positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false positives.
    '''
    return sum([(y_true[i] == False and y_pred[i] == True) for i in range(len(y_true))])

def get_true_positives(y_true:list, y_pred:list) -> int:
    '''Returns the number of true positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true positives.
    '''
    return sum([(y_true[i] == True and y_pred[i] == True) for i in range(len(y_true))])

def get_false_negatives(y_true:list, y_pred:list) -> int:
    '''Returns the number of false negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false negatives.
    '''
    return sum([(y_true[i] == True and y_pred[i] == False) for i in range(len(y_true))])

def get_true_negatives(y_true:list, y_pred:list) -> int:
    '''Returns the number of true negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true negatives.
    '''
    return sum([(y_true[i] == False and y_pred[i] == False) for i in range(len(y_true))])

def get_accuracy(y_true:list, y_pred:list) -> float:
    '''Returns the accuracy of the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         accuracy of the predictions.
    '''
    return (get_true_positives(y_true, y_pred)+get_true_negatives(y_true, y_pred))/(get_true_positives(y_true, y_pred)+get_true_negatives(y_true, y_pred)+get_false_positives(y_true, y_pred)+get_false_negatives(y_true, y_pred))

def get_precision(y_true:list, y_pred:list) -> float:
    '''Returns the precision of the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         precision of the predictions.
    '''
    return (get_true_positives(y_true, y_pred))/(get_true_positives(y_true, y_pred)+get_false_positives(y_true, y_pred))

def get_recall(y_true:list, y_pred:list) -> float:
    '''Returns the recall of the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         recall of the predictions.
    '''
    return (get_true_positives(y_true, y_pred))/(get_true_positives(y_true, y_pred)+get_false_negatives(y_true, y_pred))

def get_f1(y_true:list, y_pred:list) -> float:
    '''Returns the f1 score for the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         f1-score of the predictions.
    '''
    return 2/((1/get_recall(y_true, y_pred))+(1/get_precision(y_true, y_pred)))

def pretty_print(y_true:list, y_pred:list) -> None:
    '''Prints a confusion matrix in ascii art.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.)
    '''
    fp = f'{get_false_positives(y_true, y_pred):4d}'
    fn = f'{get_false_negatives(y_true, y_pred):4d}'
    tp = f'{get_true_positives(y_true, y_pred):4d}'
    tn = f'{get_true_negatives(y_true, y_pred):4d}'

    print( '      |    true    |')
    print( ' pred | TRUE FALSE |')
    print( '------|------------|')
    print(f' TRUE | {tp}  {fp} |')
    print(f'FALSE | {fn}  {tn} |\n')

    print(f'Accuracy: {get_accuracy(y_true, y_pred):.4f}')
    print(f'F1-score: {get_f1(y_true, y_pred):.4f}')