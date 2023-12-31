"""
Four in a row

Author: Tony Lindgren
"""
from copy import deepcopy


class FourInARow:
    def __init__(self, player, chip):
        new_board = []
        for _ in range(7):
            start_string = "_"
            new_board.append(
                [
                    start_string,
                    start_string,
                    start_string,
                    start_string,
                    start_string,
                    start_string,
                ]
            )
        self.board = new_board
        self.action = list(range(7))
        if chip != "r" and chip != "w":
            print("The provided value is not a valid chip (must be, r or w): ", chip)
        if player == "human" and chip == "w":
            self.ai_player = "r"
            self.human_player = "w"
        else:
            self.ai_player = "w"
            self.human_player = "r"
        self.curr_move = chip

    def to_move(self):
        return self.curr_move

    # actions
    # TODO
    # The action is to insert a new chip at the top of the board. This chip will be inserted at the column 1-7.
    # One constraint is that if the column is full, the chip cannot be inserted.

    def action_handler(self, column):
        if column[0] != "_":
            print("Full column!")
        else:
            count = 0
            for i in column:
                le = len(column)
                le2 = le - 1
                if column[le2] == "_":
                    column.pop()
                    column.append(self.to_move())
                    break
                elif i != "_":
                    replace_pos = count - 1
                    column[replace_pos] = self.to_move()
                    break
                else:
                    count += 1
        return column

    def result(self, action):
        dc = deepcopy(self)
        if self.to_move() == "w":
            dc.curr_move = "r"
            column = dc.board[action]
            new_column = self.action_handler(column)
            dc.board[action] = new_column
        else:
            dc.curr_move = "w"
            column = dc.board[action]
            new_column = self.action_handler(column)
            dc.board[action] = new_column
        return dc

    # eval
    # TODO
    def evaluate(self):
        score = 0
        chip = self.curr_move
        for i in range(len(self.board)):
            for j in range(6):
                if self.board[i][j] == chip:
                    score += 4 - abs(3 - i) #Score for column
                    score += 3 - min(abs(3 - j), abs(2 - j))
                elif self.board[i][j] != "_":
                    score -= 4 - abs(3 - i) #Score for column
                    score -= 3 - min(abs(3 - j), abs(2 - j))
        return score


    # inputs one row and checks for four values in a row
    def check_count(self, row, val):
        count = row.count(val)
        # print("Count:", count, " Val: ", val, " Type: ", row)
        if count >= 4:
            elem_count = 0
            for i in range(0, len(row)):
                if val == row[i]:
                    elem_count += 1
                else:
                    val = row[i]
                    elem_count = 1
                if elem_count == 4:
                    if self.ai_player == val:
                        return True, 100  # MAX ai wins positive utility
                    else:
                        return True, -100  # MIN player wins negative utility
        return False, 0

    def is_terminal(self):
        # check horizontal
        main_has_won = False
        main_util = 0
        response = main_has_won, main_util

        # creating new array of arrays with horizontal values in the same arrays
        # works as intended
        final_arr = []
        for i in range(6):
            arr = []
            for column in self.board:
                arr.append(column[i])
            final_arr.append(arr)

        # horizontal rows are created, final_arr is now list of lists with all rows and elements
        # in the same arrays
        for row in final_arr:
                has_won, util = self.check_count(row, "w")
                if has_won:
                    if util > 0:
                        print("Found horizontal win")  # MAX ai wins positive utility
                    else:
                        print(
                            "Found horizontal loss"
                        )  # MIN player wins negative utility
                    response = (has_won, util)

                has_won, util = self.check_count(row, "r")
                if has_won:
                    if util > 0:
                        print("Found horizontal win")  # MAX ai wins positive utility
                    else:
                        print(
                            "Found horizontal loss"
                        )  # MIN player wins negative utility
                    response = (has_won, util)

        # check vertical
        for column in self.board:
            has_won, util = self.check_count(column, "w")
            if has_won:
                if util > 0:
                    print("Found vertical win")  # MAX ai wins positive utility
                else:
                    print("Found vertical loss")  # MIN player wins negative utility
                response = (has_won, util)

            has_won, util = self.check_count(column, "r")
            if has_won:
                if util > 0:
                    print("Found vertical win")  # MAX ai wins positive utility
                else:
                    print("Found vertical loss")  # MIN player wins negative utility
                response = (has_won, util)

        # check vertical
        # for c in range(0, len(self.board)):
        #    count = 0
        #    curr_chip = None
        #    print("Currchip: ", self.curr_move)
        #    for r in range(0, len(self.board[c])):
        #       if curr_chip == self.board[c][r]:
        #            count = count + 1
        #            print("A")
        #            print("Currchip: ", self.curr_move)
        #        else:
        #            curr_chip = self.board[c][r]
        #            count = 1
        #            print("B")
        #            print("Currchip: ", self.curr_move)
        #        if count == 4:
        #            print("Count: ", count)
        #            if self.ai_player == curr_chip:
        #                print('Found vertical win')
        #                return True, 100          #MAX ai wins positive utility
        #            else:
        #                print('Found vertical loss')
        #                return True, -100         #MIN player wins negative utility

        # check positive diagonal
        for c in range(7-3): # * 4
            for r in range(6-3): # * 4
                if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:
                        print('Found positive diagonal win')
                        return True, 100
                    elif (self.human_player == self.board[c][r] and self.human_player == self.board[c+1][r+1]and self.human_player == self.board[c+2][r+2] and self.human_player == self.board[c+3][r+3]):
                        print('Found positive diagonal loss')
                        return True, -100

        # check negative diagonal
        # TODO
        for c in range(3, 6): # * 4
            for r in range(6-3): # * 4
                if len(self.board[c]) > r and len(self.board[c-1]) > r+1 and len(self.board[c-2]) > r+2 and len(self.board[c-3]) > r+3:
                    if self.ai_player == self.board[c][r] and self.ai_player == self.board[c-1][r+1] and self.ai_player == self.board[c-2][r+2] and self.ai_player == self.board[c-3][r+3]:
                        print('Found negative diagonal win')
                        return True, 100
                    elif self.human_player == self.board[c][r] and self.human_player == self.board[c-1][r+1] and self.human_player == self.board[c-2][r+2] and self.human_player == self.board[c-3][r+3]:
                        print('Found negative diagonal loss')
                        return True, -100

        # check draw
        # TODO
        is_full = False
        is_full_count = 0
        for c in self.board:
            for v in c:
                v_count = 0
                if v != "_":
                    v_count + 1
            if v_count == 6:
                is_full_count + 1
        if is_full_count == 7:
            is_full = True
        
        response = is_full, 0



        return response

    # pretty_print creates a new pretty board to display columns
    def pretty_print(self):
        pretty_board = [[], [], [], [], [], []]
        for i in self.board:
            for y in range(6):
                pretty_board[y].append(i[y])

        print("Pretty Board:")
        for i in pretty_board:
            print(i)
