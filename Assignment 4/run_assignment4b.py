'''
run_assignment4b.py

Author Korbinian Randl
'''

from decision_tree import BinaryDecisionTree
import metrics
import json
import string
import re

import nltk

####################################################################################################
# Functions:                                                                                       #
####################################################################################################

def count_tokens(tokens:list, columns:list=None) -> tuple:
    '''Converts the provided tokenized texts to a bag of words.

    inputs:
        tokens:     list[str] of texts to be tokenized.

        columns:    list of allowed feature names.

    
    returns: a lists of tokens for each of the texts.
    '''
    if columns is None:
        columns = []
        for entry in tokens: columns.extend(entry)
        columns = list(set(columns))
        print(f"Found {len(columns):d} unique tokens.")

    result = {column:[0]*len(tokens) for column in columns}
    for i,entry in enumerate(tokens):
        pas = 1/len(tokens[i])
        for token in entry:
            if token in result:
                result[token][i] += pas

    return result

def wordnet_pos(tag):
    if tag[0] == 'J': return nltk.corpus.wordnet.ADJ
    elif tag[0] == 'V': return nltk.corpus.wordnet.VERB
    elif tag[0] == 'N': return nltk.corpus.wordnet.NOUN
    elif tag[0] == 'R': return nltk.corpus.wordnet.ADV
    else: return nltk.corpus.wordnet.NOUN

def preprocess_text(text:str, tokenizer=None, stopWords=None, punctuation=None, stemmer=None, lemmatizer=None) -> list :
    inProcessing = text
    if (tokenizer):
        inProcessing = nltk.word_tokenize(inProcessing)
    if (stemmer):
        inProcessing = [stemmer.stem(word) for word in inProcessing]
    elif (lemmatizer):
        tags = nltk.pos_tag(inProcessing)
        inProcessing = [lemmatizer.lemmatize(tag[0].lower(), wordnet_pos(tag[1])) for tag in tags]
    if (stopWords):
        inProcessing = [word for word in inProcessing if word not in stopWords]
    if (punctuation):
        inProcessing = [word for word in inProcessing if word not in punctuation]

    
    return inProcessing

def preprocess_2(text:str, tokenizer=None, stopWords=None, punctuation=None, stemmer=None, lemmatizer=None)->list:
    inProcessing = re.sub('[^a-zA-Z]',' ', text)
    inProcessing = inProcessing.lower()
    inProcessing = inProcessing.split(' ')
    inProcessing = [word for word in inProcessing if word not in stopWords]
    tags = nltk.pos_tag(inProcessing)
    inProcessing = [lemmatizer.lemmatize(tag[0], wordnet_pos(tag[1])) for tag in tags]
    return inProcessing

class Tokenizer:
    def tokenize(text:str):
        tokens = [word for word in text.split(" ")]
        return tokens


####################################################################################################
# Load Data:                                                                                       #
####################################################################################################

with open('movies.json', 'r') as file:
    data = json.load(file)

X_train = data['text'][:1600]
y_train = data['class'][:1600]

X_test  = data['text'][1600:]
y_test  = data['class'][1600:]


####################################################################################################
# Main Function:                                                                                   #
####################################################################################################

if __name__ == '__main__':
    # print a sample of the data:
    ''' print('Cornell Movie Review Data By B. Pang et al 2005 (https://www.cs.cornell.edu/home/llee/papers/pang-lee-stars.home.html):')
    for text,label in zip(X_train[:5],y_train[:5]):
        print(f'"{text}" -> {str(label)}\n')'''



    #Preprocessing of the texts

    #With NLTK
    toke = nltk.tokenize.WordPunctTokenizer()
    stwd = set(nltk.corpus.stopwords.words('english'))
    punc = [*string.punctuation] + ['"', '``', '--']
    stem = nltk.stem.SnowballStemmer('english')
    lemm = nltk.stem.WordNetLemmatizer()
    X_train = [preprocess_2(text, tokenizer=toke, stopWords=stwd, punctuation=punc, stemmer=None, lemmatizer=lemm) for text in X_train]
    X_test  = [preprocess_2(text, tokenizer=toke, stopWords=stwd, punctuation=punc, stemmer=None, lemmatizer=lemm) for text in X_test]

    # create bag of words:
    X_train = count_tokens(X_train)
    X_test  = count_tokens(X_test, columns=list(X_train.keys()))

    # train a decision tree classifier and predict the test set:
    print('Training Decision Tree ...')
    tree = BinaryDecisionTree(X_train, y_train, max_depth=5)
    predictions_tree = tree.predict(X_test)
    print('Done.\n')

    # print decision tree:
    print('Final Decision Tree:')
    tree.pretty_print()
    print()
    
    # print confusion matrix:
    print('Performance Decision Tree:')
    metrics.pretty_print(y_test, predictions_tree)