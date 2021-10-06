board = [[1, 4, 0, 5, 0, 6, 3, 0, 0],
         [3, 0, 0, 0, 0, 0, 0, 8, 0],
         [9, 8, 2, 4, 1, 3, 0, 0, 0],
         [0, 0, 0, 8, 0, 0, 0, 0, 9],
         [0, 7, 6, 3, 0, 0, 1, 2, 0],
         [8, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 2, 3, 7, 8, 1, 5],
         [0, 5, 0, 0, 0, 0, 0, 0, 6],
         [0, 0, 8, 6, 0, 5, 0, 3, 4]]


def start_game(board):
    """
    Prints the starting game board and prompts instructions to the user.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print('')
    print('')
    print('Welcome! Below you will see prompts each time you would like to enter a number into the puzzle. \n')
    print('Once you believe you have solved the puzzle, enter -1 when asked to specify a column, and the program will '
          'verify your inputs and give '
          'you a result. \n')
    return inputs()


def inputs():
    """
    Displays board and input prompts to console to update the board accordingly.
    """
    column = int(input('Please enter the column of your entry (1-9): \n'))
    if column == -1:
        if check_game(board) is True:
            print('Solved!')
            return
        else:
            print('Not solved, try again!\n')
            for i in range(len(board)):
                for j in range(len(board)):
                    print(board[i][j], end=" ")
                print('')
            print('')
            return inputs()
    else:
        row = int(input('Please enter the row of your entry (1-9): \n'))
        number = int(input('Please enter what number you would like to input: \n'))
        print('')
        board[row - 1][column - 1] = number
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=" ")
            print('')
        print('')
        return inputs()


def check_game(board):
    """
    Checks the finished Sudoku board to see if a correct solution was found and returns True, False if otherwise.
    """
    # checks columns and rows first
    for i in range(len(board)):
        row_sum = 0
        column_sum = 0
        for j in range(len(board)):
            # verify numbers are within range 1-9 inclusive
            if board[i][j] < 1 or board[i][j] > 9:
                return False
            # column sum
            column_sum += board[j][i]
            # row sum
            row_sum += board[i][j]
        if column_sum != 45 or row_sum != 45:
            return False
    # block sums
    for i in range(3):
        for j in range(3):
            block_sum = 0
            for k in range(3):
                for l in range(3):
                    block_sum += board[i * 3 + k][j * 3 + l]
                    # verify numbers are within 1-9 inclusive
                    if board[i][j] < 1 or board[i][j] > 9:
                        return False
            if block_sum != 45:
                return False
    return True

if __name__ == '__main__':
    start_game(board)
