'''
Four in a row

Author: Tony Lindgren
'''
from copy import deepcopy

class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            start_string = "_"
            new_board.append([start_string, start_string, start_string, start_string, start_string, start_string])
        self.board = new_board
        self.action = list(range(7))
        print("Action: ", self.action)
        if chip != 'r' and chip != 'w':
            print('The provided value is not a valid chip (must be, r or w): ', chip)
        if player == 'human' and chip == 'w':
            self.ai_player = 'r'
        else:
            self.ai_player = 'w'
        self.curr_move = chip
    
    def to_move(self):
        return self.curr_move

    #actions
    #TODO
    # The action is to insert a new chip at the top of the board. This chip will be inserted at the column 1-7.
    # One constraint is that if the column is full, the chip cannot be inserted.

    def result(self, action):           
        dc = deepcopy(self)
        if self.to_move() == 'w':
            dc.curr_move = 'r'
            column = dc.board[action]
            if column[0] != "_":
                print("Full column!")
            else:
                column.pop()
                column.append(self.to_move())
        else:
            dc.curr_move = 'w'
            dc.board[action].append(self.to_move())            
        return dc
        
    #eval
    #TODO
        
    def is_terminal(self):
        #check vertical
        for c in range(0, len(self.board)):
            count = 0
            curr_chip = None
            print("Currchip: ", self.curr_move)
            for r in range(0, len(self.board[c])):
                if curr_chip == self.board[c][r]:
                    count = count + 1
                else:
                    curr_chip = self.board[c][r]     
                    count = 1
                if count == 4:
                    if self.ai_player == curr_chip:    
                        print('Found vertical win')
                        return True, 100          #MAX ai wins positive utility
                    else:
                        print('Found vertical loss')
                        return True, -100         #MIN player wins negative utility
                    
        #check horizontal 
        #TODO

                    
        #check positive diagonal
        for c in range(7-3): 
            for r in range(6-3):    
                if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:  
                        print('Found positive diagonal win')
                        return True, 100
                    elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r+1] and self.ai_player != self.board[c+2][r+2] and self.ai_player != self.board[c+3][r+3]:  
                        print('Found positive diagonal loss')
                        return True, -100
        
        #check negative diagonal 
        #TODO   
             
        #check draw
        #TODO  
         
        return False, 0                                            
                
    #pretty_print
    #TODO
    # creates a new pretty board to display columns
    def pretty_print(self):
        pretty_board = [[], [], [], [], [], []]
        for i in self.board:
            for y in range (6):
                pretty_board[y].append(i[y])
        
        print("Pretty Board:")
        for i in pretty_board:
            print(i)
        
        #print("Self.board: ")
        #for i in self.board:
        #    print(i)