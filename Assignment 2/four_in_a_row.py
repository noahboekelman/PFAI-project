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
        else:
            self.ai_player = "w"
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

    # inputs one row and checks for four values in a row
    def check_count(self, row, val):
        count = row.count(val)
        if count >= 4:
            elem_count = 0
            for i in range(0, len(row)):
                if val == row[i]:
                    elem_count += 1
                else:
                    val = row[i]
                    elem_count = 1
                if elem_count == 4:
                    print("Elem count plus: ", elem_count)
                    print(val)
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
            if "w" in row:
                has_won, util = self.check_count(row, "w")
                if has_won:
                    if util > 0:
                        print("Found horizontal win")  # MAX ai wins positive utility
                    else:
                        print(
                            "Found horizontal loss"
                        )  # MIN player wins negative utility
                    response = (has_won, util)

            elif "r" in row:
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
        # for c in range(7-3):
        #    for r in range(6-3):
        #       if len(self.board[c]) > r and len(self.board[c+1]) > r+1 and len(self.board[c+2]) > r+2 and len(self.board[c+3]) > r+3:
        #            if self.ai_player == self.board[c][r] and self.ai_player == self.board[c+1][r+1] and self.ai_player == self.board[c+2][r+2] and self.ai_player == self.board[c+3][r+3]:
        #                print('Found positive diagonal win')
        #                return True, 100
        #            elif self.ai_player != self.board[c][r] and self.ai_player != self.board[c+1][r+1] and self.ai_player != self.board[c+2][r+2] and self.ai_player != self.board[c+3][r+3]:
        #                print('Found positive diagonal loss')
        #                return True, -100

        # check negative diagonal
        # TODO

        # check draw
        # TODO
        return response

    # pretty_print
    # TODO
    # creates a new pretty board to display columns
    def pretty_print(self):
        pretty_board = [[], [], [], [], [], []]
        for i in self.board:
            for y in range(6):
                pretty_board[y].append(i[y])

        print("Pretty Board:")
        for i in pretty_board:
            print(i)

        # print("Self.board: ")
        # for i in self.board:
        #    print(i)
