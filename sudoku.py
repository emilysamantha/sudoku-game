import doctest
import math
import copy
from random import randrange
from random import choice

# Sudoku boards
small = [[1, 0, 0, 0],
         [0, 4, 1, 0],
         [0, 0, 0, 3],
         [4, 0, 0, 0]]

small2 = [[0, 0, 1, 0],
          [4, 0, 0, 0],
          [0, 0, 0, 2],
          [0, 3, 0, 0]]

big = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
       [4, 0, 0, 7, 8, 9, 0, 0, 0],
       [7, 8, 0, 0, 0, 0, 0, 5, 6],
       [0, 2, 0, 3, 6, 0, 8, 0, 0],
       [0, 0, 5, 0, 0, 7, 0, 1, 0],
       [8, 0, 0, 2, 0, 0, 0, 0, 5],
       [0, 0, 1, 6, 4, 0, 9, 7, 0],
       [0, 0, 0, 9, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 3, 0, 0, 0, 2]]

big2 = [[7, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 0, 3, 0, 0, 4, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 8],
        [6, 2, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 7, 0],
        [0, 0, 0, 6, 0, 0, 9, 8, 0],
        [0, 0, 0, 0, 2, 7, 3, 0, 0],
        [0, 0, 2, 0, 8, 0, 0, 5, 0]]

big3 = [[0, 0, 8, 1, 9, 0, 0, 0, 6],
        [0, 4, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 6, 0, 0, 1, 3, 0],
        [0, 0, 6, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 3, 0, 9, 0, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 5, 7]]

big4 = [[0, 0, 0, 6, 0, 0, 2, 0, 0],
        [8, 0, 4, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [4, 0, 5, 0, 0, 0, 0, 0, 7],
        [7, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 5, 0, 0, 0, 8],
        [3, 0, 0, 0, 7, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 6, 0]]

giant = [[0,  0, 13,  0,  0,  0,  0,  0,  2,  0,  8,  0,  0,  0, 12, 15],
         [7,  8, 12,  2, 10,  0,  0, 13,  0,  0, 14, 11,  6,  9,  0,  4],
         [11, 10,  0,  0,  0,  6, 12,  5,  0,  3,  0,  0,  0, 14,  0,  8],
         [1,  0,  0,  0, 14,  0,  2,  0,  0,  4,  6,  0, 16,  3,  0, 13],
         [12,  6,  0,  3,  0,  0, 16, 11,  0, 10,  1,  7, 13, 15,  0,  0],
         [0, 13,  0,  0,  0, 15,  8,  0, 14,  0,  0,  0,  0, 16,  5, 11],
         [8,  0, 11,  9, 13,  0,  7,  0,  0,  0,  0,  3,  2,  4,  0, 12],
         [5,  0,  0, 16, 12,  9,  0, 10, 11,  2, 13,  0,  0,  0,  8,  0],
         [0,  0,  0,  0, 16,  8,  9, 12,  0,  0,  0,  0,  0,  6,  3,  0],
         [2, 16,  0,  0,  0, 11,  0,  0,  7,  0, 12,  6,  0, 13, 15,  0],
         [0,  0,  4,  0,  0, 13,  0,  7,  3, 15,  0,  5,  0,  0,  0,  0],
         [0,  7,  0, 13,  4,  5, 10,  0,  1,  0, 11, 16,  9,  0, 14,  2],
         [0,  2,  8,  0,  9,  0,  0,  0,  4,  0,  7,  0,  0,  5,  0,  0],
         [14,  0,  0,  0, 15,  2, 11,  4,  9, 13,  3,  0, 12,  0,  0,  0],
         [0,  1,  9,  7,  0,  0,  5,  0,  0, 11, 15, 12,  0,  0,  0,  0],
         [16,  3, 15,  0,  0, 14, 13,  6, 10,  1,  0,  2,  0,  8,  4,  9]]

giant2 = [[0,  5,  0,  0,  0,  4,  0,  8,  0,  6,  0,  0,  0,  0,  9, 16],
          [1,  0,  0,  0,  0,  0,  0, 13,  4,  0,  0,  7, 15,  0,  8,  0],
          [13,  0,  0,  0,  0,  7,  3,  0,  0,  0,  0,  9,  5, 10,  0,  0],
          [0, 11, 12, 15, 10,  0,  0,  0,  0,  0,  5,  0,  3,  4,  0, 13],
          [15,  0,  1,  3,  0,  0,  7,  2,  0,  0,  0,  0,  0,  5,  0,  0],
          [0,  0,  0, 12,  0,  3,  0,  5,  0, 11,  0, 14,  0,  0,  0,  9],
          [4,  7,  0,  0,  0,  0,  0,  0, 12,  0, 15, 16,  0,  0,  0,  0],
          [0,  0,  0,  0, 14,  0, 15,  0,  6,  9,  0,  0,  0,  0, 12,  0],
          [3,  0, 15,  4,  0, 13, 14,  0,  0,  0,  0,  1,  0,  0,  7,  8],
          [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9, 10,  0,  0,  0,  0],
          [11,  0, 16, 10,  0,  0,  0,  0,  0,  7,  0,  0,  0,  3,  5,  0],
          [0,  0, 13,  0,  0,  0,  0,  0, 14,  0, 16, 15,  0,  9,  0,  1],
          [9,  0,  2,  0,  0, 14,  0,  4,  8,  0,  0,  0,  0,  0,  0,  0],
          [0, 14,  0,  0,  0,  0,  0, 10,  9,  0,  3,  0,  0,  0,  1,  7],
          [8,  0,  0,  0, 16,  0,  0,  1,  2, 14, 11,  4,  0,  0,  0,  3],
          [0,  0,  0,  1,  0,  0,  5,  0,  0, 16,  0,  6,  0, 12,  0,  0]]

giant3 = [[0,  4,  0,  0,  0,  0,  0, 12,  0,  1,  0,  0,  9,  0,  8,  0],
          [15, 14,  0,  0,  9,  0,  0, 13,  8,  0,  0, 10,  1,  0,  0,  0],
          [0,  7,  0,  0,  0,  0,  0,  8, 16,  0, 14,  0,  0,  2,  0,  0],
          [0,  0,  0,  9,  0,  0, 11,  0,  0,  0,  0,  0,  5,  0,  0, 15],
          [3,  0, 12,  0,  7,  0, 10,  0,  0, 11,  2,  0,  0,  0,  0,  6],
          [14,  8,  0,  0,  0, 12,  0,  6,  0,  0,  0, 16,  0,  0,  0, 10],
          [0, 16,  0,  0, 13,  0,  0,  0,  0,  0,  0,  0,  0,  0, 12,  0],
          [6,  0,  0,  0,  0,  8,  0,  5,  1,  7, 13,  0, 11,  0,  0, 14],
          [0,  0,  0,  2,  0,  0, 16,  0, 15, 12,  0,  3, 10,  7,  0,  0],
          [0,  9,  0,  5, 11,  0,  3,  0,  4, 13, 16,  0,  0, 15,  6,  0],
          [0,  0,  0,  0,  5,  4,  0,  0,  9,  6,  0,  2,  0,  0,  0,  0],
          [1,  0,  0,  0,  0, 15, 12,  0,  0,  0,  5,  0,  0,  0,  9,  0],
          [12, 10,  0, 15,  0,  1,  0,  0,  2,  9,  3,  4,  0,  0,  5,  0],
          [0,  0,  0,  3, 10,  0,  4,  0,  0, 15,  0,  0,  0,  0,  0,  0],
          [0,  0,  0,  0, 16,  0,  0,  0,  0,  0,  0,  0,  0,  0, 10, 11],
          [11,  6,  8,  0,  0,  0, 15,  0, 14,  0,  0,  0,  0, 13,  0,  2]]

sudoku_boards = [[], [], [small, small2], [big, big2, big3, big4], [giant, giant2, giant3]]


def board_size(board: list) -> int:
    """
    Input:
        board: Sudoku board

    Output:
        Length of the sudoku board and the length of the subgrid
    """
    return len(board), int(math.sqrt(len(board)))


def print_board(board: list) -> None:
    """
    Prints a given board to the console in a way that aligns the content of columns and makes
    the subgrids visible.

    Input:
        board: Sudoku board of size 4x4, 9x9, or 16x16

    For example:

    >>> print_board(small2)
    -------
    |  |1 |
    |4 |  |
    -------
    |  | 2|
    | 3|  |
    -------
    >>> print_board(big)
    -------------
    |   |   |   |
    |4  |789|   |
    |78 |   | 56|
    -------------
    | 2 |36 |8  |
    |  5|  7| 1 |
    |8  |2  |  5|
    -------------
    |  1|64 |97 |
    |   |9  |   |
    |   | 3 |  2|
    -------------
    >>> print_board(giant2)
    ---------------------
    | 5  | 4 8| 6  |  9G|
    |1   |   D|4  7|F 8 |
    |D   | 73 |   9|5A  |
    | BCF|A   |  5 |34 D|
    ---------------------
    |F 13|  72|    | 5  |
    |   C| 3 5| B E|   9|
    |47  |    |C FG|    |
    |    |E F |69  |  C |
    ---------------------
    |3 F4| DE |   1|  78|
    |    |    |  9A|    |
    |B GA|    | 7  | 35 |
    |  D |    |E GF| 9 1|
    ---------------------
    |9 2 | E 4|8   |    |
    | E  |   A|9 3 |  17|
    |8   |G  1|2EB4|   3|
    |   1|  5 | G 6| C  |
    ---------------------
    """
    # Setting n and k based on board size
    n, k = board_size(board)

    # Determining the length of the line
    line = '-' * (1+n+k)

    # Printing contents of the board
    for row in range(n):
        # Printing row dividers
        if row % k == 0:
            print(line)
        for col in range(n):
            # Printing column dividers
            if col % k == 0:
                print('|', end='')
            # Printing an empty space, the number, or the hint
            if board[row][col] == 0:
                print(' ', end='')
            elif board[row][col] == '*':
                print('*', end='')
            elif board[row][col] > 9:
                # If the number is 10 or larger, print the letter codes
                print(chr(board[row][col] + 55), end='')
            else:
                print(board[row][col], end='')
        # Printing divider at the end of each row
        print('|')

    print(line)  # Bottom line


def subgrid_values(board: list, row_index: int, column_index: int) -> list:
    """
    Input:
        board: Sudoku board
        row_index: row number of the spot (starting from 0)
        column_index: column number of the spot (starting from 0)
    Output:
        res: List of all numbers that are present in the subgrid of the given spot

    For example:

    >>> subgrid_values(small2, 1, 3)
    [1]
    >>> subgrid_values(big, 4, 5)
    [3, 6, 7, 2]
    >>> subgrid_values(giant2, 4, 5)
    [7, 2, 3, 5, 14, 15]
    """
    # Setting n and k based on board size
    n, k = board_size(board)

    # Determining location of element
    subgrid_row = row_index // k
    subgrid_col = column_index // k

    # Appending values to result list
    res = []
    for i in range(k):
        for j in range(k):
            num = board[subgrid_row*k+i][subgrid_col*k+j]
            if num != 0:
                res.append(num)

    return res


def options(board: list, i, j):
    """
    Input:
        board: Sudoku board
        row_index: row number of the spot (starting from 0)
        column_index: column number of the spot (starting from 0)
    Output:
        res: List of all numbers that the player is allowed to place on the spot (row_index, column_index),
             i.e., those that are not already present in row row_index, column (column_index), and subgrid of
             the spot (row_index, column_index)

    For example:

    >>> options(small2, 0, 0)
    [2, 3]
    >>> options(big, 6, 8)
    [3, 8]
    >>> options(giant2, 1, 5)
    [2, 5, 6, 9, 11, 12, 16]
    """
    # Creating list of numbers present in row i and column j
    row_nums = []
    col_nums = []
    n = len(board)
    for val in range(n):
        if board[i][val] != 0:
            row_nums.append(board[i][val])
        if board[val][j] != 0:
            col_nums.append(board[val][j])

    # Appending values not in the subgrid, row, or column of (i, j) to the result list
    res = []
    for num in range(1, n+1):
        if num not in subgrid_values(board, i, j) and num not in row_nums and num not in col_nums:
            res.append(num)

    return res


def hint(board: list) -> None:
    """
    Prints a hint on the given sudoku board.
    The hint is determined by the spot with the least number of options.

    Input:
        board: Sudoku board to print a hint on
    """
    n = len(board)
    curr_row = 0
    curr_col = 0
    num_opt = n

    # Determining the spot with the least options
    for row in range(n):
        for col in range(n):
            if board[row][col] == 0 and len(options(board, row, col)) < num_opt:
                curr_row = row
                curr_col = col
                num_opt = len(options(board, row, col))

    # Modifying the board to show the hint
    board[curr_row][curr_col] = '*'

    # Printing the board with the hint
    print("SHOWING HINT")
    print_board(board)
    print(f"({curr_row}, {curr_col})")


def play(board: list) -> None:
    """
    Main game function that allows user to play the sudoku board via console

    Input:
        board: Sudoku board
    """
    # Keep record of the board we started with for if the player wants to restart
    restart_board = copy.deepcopy(board)

    # Main game loop
    # Printing the action options list
    print("Action option -> input format:")
    print("1. Fill a spot -> <row> <column> <number_to_fill>")
    print("2. Choose a new sudoku board from the list of sudoku boards -> n <length_of_subgrid> <choice>")
    print("3. Infer the current board -> i")
    print("4. Generate a new sudoku board -> g <length_of_subgrid>")
    print("5. Undo a move -> u")
    print("6. Get a hint -> h")
    print("7. Restart the board -> r")
    print("8. Quit the game -> q")

    unsolved = True
    while unsolved:
        # Print the sudoku board
        print_board(board)

        # Get player's input
        valid_input = False
        while not valid_input:
            # Prompt the player's input
            player_input = input("Enter an action: ").split(' ')

            # 1. If the player wants to fill a spot
            if len(player_input) == 3 and \
                    player_input[0].isdecimal() and \
                    player_input[1].isdecimal() and \
                    player_input[2].isdecimal():
                row = int(player_input[0])
                column = int(player_input[1])
                num = int(player_input[2])

                # Checking if the spot to fill is valid
                if board[row][column] == 0 and num in options(board, row, column):
                    board[row][column] = num
                    valid_input = True
                else:
                    print("Please enter a valid spot to fill in the format -> <row> <column> <number>")

            # 2. If the player wants to choose a new sudoku board from the list of sudoku boards
            elif len(player_input) == 3 and \
                    (player_input[0] == 'n' or player_input[0] == 'new') and \
                    player_input[1].isdecimal() and \
                    player_input[2].isdecimal():
                k = int(player_input[1])
                d = int(player_input[2])
                if k < len(sudoku_boards) and 0 < d <= len(sudoku_boards[k]):
                    board = sudoku_boards[k][d - 1]
                    valid_input = True
                else:
                    print('Please enter a valid board in the format -> n <length_of_subgrid> <choice>')

            # 3. If the player wants to infer the current board
            elif player_input[0] == 'i' or player_input[0] == 'infer':
                valid_input = True
                print("Inferred board:")
                print_board(inferred(board))

            # 4. If the player wants to generate a new sudoku board
            elif (player_input[0] == 'g' or player_input[0] == 'generate') and player_input[1].isdecimal():
                valid_input = True
                k = int(player_input[1])
                board = generate(k)

            # 5. If the player wants to undo a move
            elif player_input[0] == 'u' or player_input[0] == 'undo':
                valid_input = True
                board[row][column] = 0

            # 6. If the player wants to get a hint
            elif player_input[0] == 'h' or player_input[0] == 'hint':
                valid_input = True
                hint(board)

            # 7. If the player wants to restart the game
            elif player_input[0] == 'r' or player_input[0] == 'restart':
                valid_input = True
                board = restart_board

            # 8. If the player wants to quit the game
            elif player_input[0] == 'q' or player_input[0] == 'quit':
                valid_input = True
                unsolved = False
                print('Thank you for playing Sudoku! See you later!')

            # Any other input is invalid
            else:
                print('Sorry, you have entered an invalid input.')
                print("Please choose an action from the list and enter the correct format.")

        # Check for empty value in the sudoku board
        found_empty = check_empty(board)

        # If an empty spot is not found, then the board is solved and the game loop is terminated
        if not found_empty:
            print("Congratulations! You have solved the Sudoku!")
            unsolved = False


def check_empty(board: list) -> bool:
    """
    Checks the board for empty spots.
    Returns True if a spot is still filled with 0 (empty), returns False if all spots have been filled.
    """
    # Go through each spot on the sudoku board
    for row in range(len(board)):
        for col in range(len(board)):
            # If found a spot that is still empty (filled with 0), return True
            if board[row][col] == 0:
                return True
    return False


def solutions(board: list) -> list:
    def empty_fields(board: list) -> list:
        n = len(board)
        res = []
        for i in range(n):
            for j in range(n):
                if not board[i][j]:
                    res.append((i, j))
        return res

    def number_of_options(f):
        i, j = f
        return len(options(board, i, j))

    fields = empty_fields(board)
    if not fields:
        return [board]

    fields = sorted(fields, key=number_of_options)

    res = []
    i, j = fields[0]
    opts = options(board, i, j)

    for o in opts:
        _board = copy.deepcopy(board)
        _board[i][j] = o
        res += solutions(_board)
        if len(res) >= 2:
            return res
    return res


def forward_single(board: list) -> bool:
    """
    Modifies the given board by forward single inference (i.e. if a spot
    only has one option, then the answer to that spot must be the option)

    Input:
        board: Sudoku board
    Output:
        found: A boolean that tells whether a spot with one option is found
    """
    n = len(board)
    found = False

    for row in range(n):
        for col in range(n):
            # If the spot is empty and only has one option, set the spot as that number
            if board[row][col] == 0 and len(options(board, row, col)) == 1:
                answer = options(board, row, col)
                board[row][col] = answer[0]
                found = True
    return found


def backward_single_rc(board: list) -> bool:
    """
    Modifies the given board by row and column backward single inference (i.e.
    if an option only appears once in a row or column, then it must be the answer for
    the spot in which it appears)

    Input:
        board: Sudoku board
    Output:
        found: A boolean that tells whether a backward single inference is found
    """
    n = len(board)
    found = False

    for i in range(n):
        # Initializing the options list for each row and column
        row_options = []
        col_options = []

        # Appending the options for each empty spot in the row or column
        for j in range(n):
            # Row
            if board[i][j] == 0:
                for opt in options(board, i, j):
                    row_options.append(opt)
            # Column
            if board[j][i] == 0:
                for opt in options(board, j, i):
                    col_options.append(opt)

        # Creating list of options that only appear once in a row or column
        row_unique = [
            opt for opt in row_options if row_options.count(opt) == 1]
        col_unique = [
            opt for opt in col_options if col_options.count(opt) == 1]

        # Going through the row or column to set the result
        for j in range(n):
            # Row
            if board[i][j] == 0:
                for ans in row_unique:
                    if ans in options(board, i, j):
                        board[i][j] = ans
                        found = True
            # Column
            if board[j][i] == 0:
                for ans in col_unique:
                    if ans in options(board, j, i):
                        board[j][i] = ans
                        found = True

    return found


def backward_single_sg(board) -> bool:
    """
    Modifies the given board by subgrid backward single inference (i.e.
    if an option only appears once in a subgrid, then it must be the answer for
    the spot in which it appears)

    Input:
        board: Sudoku board
    Output:
        found: A boolean that tells whether a backward single inference is found
    """
    k = int(math.sqrt(len(board)))
    found = False

    # Iterating through each subgrid
    for subgrid_row in range(k):
        for subgrid_col in range(k):
            # Initializing the options list for each
            subgrid_options = []
            for i in range(k):
                for j in range(k):
                    # Appending the options for each empty spot in the subgrid
                    if board[subgrid_row*k+i][subgrid_col*k+j] == 0:
                        for opt in options(board, subgrid_row*k+i, subgrid_col*k+j):
                            subgrid_options.append(opt)

            # Creating list of options that only appear once in a subgrid
            subgrid_unique = [
                opt for opt in subgrid_options if subgrid_options.count(opt) == 1]

            # Going through the subgrid to set the result
            for i in range(k):
                for j in range(k):
                    if board[subgrid_row*k+i][subgrid_col*k+j] == 0:
                        for ans in subgrid_unique:
                            if ans in options(board, subgrid_row*k+i, subgrid_col*k+j):
                                board[subgrid_row*k+i][subgrid_col*k+j] = ans
                                found = True
    return found


def inferred(board: list) -> list:
    """
    Input:
        board: Sudoku board
    Output:
        res: A new Soduko board with all values field from input board plus
             all values that can be inferred by repeated application of
             forward and backward single rule

    For example board big can be completely inferred:

    >>> inferred(big) # doctest: +NORMALIZE_WHITESPACE
    [[2, 1, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [1, 2, 4, 3, 6, 5, 8, 9, 7],
    [3, 6, 5, 8, 9, 7, 2, 1, 4],
    [8, 9, 7, 2, 1, 4, 3, 6, 5],
    [5, 3, 1, 6, 4, 2, 9, 7, 8],
    [6, 4, 2, 9, 7, 8, 5, 3, 1],
    [9, 7, 8, 5, 3, 1, 6, 4, 2]]

    But function doesn't modify input board:

    >>> big # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 7, 8, 9, 0, 0, 0],
     [7, 8, 0, 0, 0, 0, 0, 5, 6],
     [0, 2, 0, 3, 6, 0, 8, 0, 0],
     [0, 0, 5, 0, 0, 7, 0, 1, 0],
     [8, 0, 0, 2, 0, 0, 0, 0, 5],
     [0, 0, 1, 6, 4, 0, 9, 7, 0],
     [0, 0, 0, 9, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 0, 0, 2]]

    In board big4 there is nothing to infer:

    >>> inferred(big4) # doctest: +NORMALIZE_WHITESPACE
    [[0, 0, 0, 6, 0, 0, 2, 0, 0],
     [8, 0, 4, 0, 3, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 9, 0, 0, 0],
     [4, 0, 5, 0, 0, 0, 0, 0, 7],
     [7, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 3, 0, 5, 0, 0, 0, 8],
     [3, 0, 0, 0, 7, 0, 0, 0, 4],
     [0, 0, 0, 0, 0, 1, 9, 0, 0],
     [0, 0, 0, 2, 0, 0, 0, 6, 0]]
    """
    # Copying the given sudoku board
    res = copy.deepcopy(board)

    # While either one of the 3 checks can still infer, repeat the inference process
    # Stop inferring until all three checks find nothing to infer
    found = True
    while found:
        found = False

        # Checking if there is only one option for that spot
        found = forward_single(res)

        # Checking if an option is only present in one spot in each row or column
        found = backward_single_rc(res)

        # Checking if an option is only present in one spot in a subgrid
        found = backward_single_sg(res)

    return res


def generate_full(k: int) -> list:
    """
    Generates a fully filled sudoku board.

    Input:
        k: Board size
    Output:
        board: A k^2 by k^2 completely filled sudoku board that satisfies the rules
    """
    n = k * k
    complete = False

    while not complete:
        # Generating empty board
        new_board = [None] * n
        for i in range(n):
            new_board[i] = [0] * n

        failed = False

        for i in range(n):
            for j in range(n):
                # If the length of options is 0, it means an error is encountered
                # If so, restart from an empty board
                if len(options(new_board, i, j)) == 0:
                    failed = True
                    break
                new_board[i][j] = choice(options(new_board, i, j))
            if failed:
                break

        if failed:
            continue

        return new_board


def remove_spots(board: list) -> list:
    """
    Removes as many random spots in the sudoku board as possible, such that it would still have a unique solution.
    Input:
        board: A full sudoku board
    Output:
        board: A partially removed sudoku board
    """
    n = len(board)
    # While the board still has a unique solution
    while len(solutions(board)) == 1:
        # Picking a random spot on the board
        i = randrange(0, n)
        j = randrange(0, n)

        # Copy the board to check the vailidity
        try_res = copy.deepcopy(board)
        try_res[i][j] = 0
        if len(solutions(try_res)) == 0:
            # If removing the spot makes the board unsolvable, choose another spot
            continue
        if len(solutions(try_res)) > 1:
            # Return the board once removing another spot makes the board have more than one solution
            return board
        board[i][j] = 0


def count_filled(board: list) -> int:
    """
    Input:
        board: The sudoku board to count
    Output:
        total: The number of filled spots in the sudoku board
    """
    total = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                total += 1
    return total


def generate(k: int) -> list:
    """
    Input:
        k: Size of the board
    Output:
        board: A new partially filled Sudoku board that has a unique solution
    For example:
    >>> len(solutions(generate(2)))
    1
    >>> len(solutions(generate(3)))
    1
    """
    board = remove_spots(generate_full(k))

    # To make sure not more than half the sudoku board is filled
    while count_filled(board) > ((k**4) // 2):
        board = remove_spots(generate_full(k))

    return board


play(big)
