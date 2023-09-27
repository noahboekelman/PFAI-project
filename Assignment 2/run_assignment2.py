'''
Define game and start execution of game search

Author: Tony Lindgren
'''
from four_in_a_row import FourInARow
#from game_node_and_game_search import GameSearch
    
def ask_ai(state0):
    #gs = GameSearch(state0, depth=3)
    #move = gs.minimax_search()
    #gs = GameSearch(state0, depth=3, time=20)
    #move = gs.mcts()
    move = input("Mr AI, what column 0-6?")
    try:
        converted_move = int(move)
        if converted_move > 6:
            print("Enter a valid digit 0-6!")
    except ValueError:
        print("Enter a valid digit 0-6!")
    else:
        state1 = state0.result(converted_move)
        print('--------')
        print('AI moves')
        print('--------')
        state1.pretty_print()  
        stop, value = state1.is_terminal() 
        if stop == True:
            if value > 0:
                print('AI won')                       
            else:
                print('Human won')
            return state1, True
        return state1, False

def ask_player(state0):
    move = input('Please choose column 0-6: ')
    try:
        converted_move = int(move)
        if converted_move > 6:
            print("Enter a valid digit 0-6!")
    except ValueError:
        print("Enter a valid digit 0-6!")
    else:
        state1 = state0.result(converted_move)
        print('--------')
        print('Player moves')
        print('--------')
        state1.pretty_print()
        stop, value = state1.is_terminal()
        if stop == True:
            if value > 0:
                print('AI won')                       
            else:
                print('Human won')
            return state1, True
        return state1, False

def main():
    print('Welcome to play four-in-a-row!')
    answer = None
    while answer != 'y' and answer != 'n':
        answer = input('Would you like to start [y/n]: ')        
    if(answer == 'y'):  
        state0 = FourInARow('human', 'w') 
        stop = False
        while not stop:            
        #Ask player         
            state1, stop1 = ask_player(state0)
            if stop1:
                break
            else:
        #AI move
                state0, stop2 = ask_ai(state1)  
                if stop2:
                    break                
    else:
        state0 = FourInARow('ai','w') 
        stop = False
        while not stop: 
        #AI move
            state1, stop1 = ask_ai(state0)    
            if stop1:
                break
            else:  
        #Ask player
                state0, stop2 = ask_player(state1)    
                if stop2:
                    break               
       
if __name__ == "__main__":
    main()