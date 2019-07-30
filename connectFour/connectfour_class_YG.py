# Project: connect four

# Description: write python script to implement framework
# 1. construct the matrix to store the current data, 7 column 6 row
# 2. ask the user to input column number to indicate where to put the point
# 3. print matrix each time after input
# 3. if the top is touched, print error
# class version


import numpy as np

# define interface class
# take input: matrix size, selected col
# record user_id


class Interface:

    def __init__(self):
        self.row_num = self._input_matrix_row()
        self.col_num = self._input_matrix_row()
        self.user_id = 1
        self.count = 0

    def _input_matrix_row(self):
        var = input("Please input row number of board: ")
        return int(var)

    def _input_matrix_col(self):
        var = input("Please input column number of board: ")
        return int(var)

    def select_col(self):
        var = input("Please specify column: ")
        return int(var)

    def update_user_id(self):
        self.count += 1
        if self.count % 2 == 0:
            self.user_id = 1
        else:
            self.user_id = 2



# define connectfour class
# input: size of matrix, user_id(1 or 2),
class ConnectFour:

    def __init__(self, row_num, col_num):
        self.row_num = row_num
        self.col_num = col_num
        self.matrix = np.zeros(shape=(self.row_num, self.col_num))
        self.row_bound = row_num - 1
        self.col_bound = col_num - 1
        # list of cols that is full
        self.invalid_col = []
        self.move = False

    def find_top_row_with_inputcol(self, input_col):
        if self.matrix[self.row_bound, input_col] == 0:
            return self.row_bound
        else:
            i = 0
            while self.matrix[i, input_col] == 0:
                i += 1
            return i - 1

    def _find_invalid_col(self, input_col):
        if self.matrix[0, input_col] != 0:
            self.invalid_col.append(input_col)

    def check_win(self, input_row, input_col, id):
        max_steps = max(self.row_bound, self.col_bound)
        direction = [[0, -1], [-1, 0], [1, -1], [-1, -1]]

        for d in direction:
            steps = 1
            score = 1
            #print("direction: "+str(d))
            while steps <= max_steps:
                x1, y1 = input_row + steps*d[0], input_col + steps*d[1]
                #print(x1, y1)
                if 0 <= x1 <= self.row_bound and 0 <= y1 <= self.col_bound:
                    #print("enter1")
                    if self.matrix[x1, y1] == id:
                        #print("enter2")
                        score += 1
                x2, y2 = input_row - steps*d[0], input_col - steps*d[1]
                if 0 <= x2 <= self.row_bound and 0 <= y2 <= self.col_bound:
                    if self.matrix[x2, y2] == id:
                        score += 1
                steps += 1
                #print("scores: " + str(score))
            if score == 4:
                return "win"
        return "not win"




    # take input from user and update matrix
    def update_matrix(self, input_col, input_row, id):

        self._find_invalid_col(input_col)
        if input_col in self.invalid_col:
            print("Column full! Please re-select ^^")
            self.move = False
        
        else:
            self.matrix[input_row, input_col] = id
            self.move = True
            print(self.matrix)

    def check_boudry(self, input_col):
        if 0 <= input_col <= self.col_bound:
            return True


def main():
    user_interface = Interface()
    game = ConnectFour(user_interface.row_num, user_interface.col_num)
    while True:
        user_input_col = user_interface.select_col()
        # break if top row is all filled
        if 0 not in game.matrix[0]:
            print("Top row is full. Game over")
            break
        elif not game.check_boudry(user_input_col):
            print("Column out of range! Please re-select")
            continue
        else:
            # TODO: check whether the input is valid here before moving
            user_input_row = game.find_top_row_with_inputcol(user_input_col)
            print("input col: " + str(user_input_col) + " input row: " + str(user_input_row))
            game.update_matrix(user_input_col, user_input_row, user_interface.user_id)
            if game.move:
                # TODO: store the input row
                if game.check_win(user_input_row, user_input_col, user_interface.user_id) == "win":
                    print("Game over. User ", user_interface.user_id, " wins.")
                    break
                else:
                    user_interface.update_user_id()




if __name__ == '__main__':
    main()
