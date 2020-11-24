def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    return board


def get_move(board, player):
    def get_move(board):
    """Returns the coordinates of a valid move for player on board."""
    allowed = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    coordinate = input("Give a coordinate: ")
    if coordinate.casefold() == 'quit':
        quit()
    row, col = 0, 0
    while coordinate.upper() not in allowed:
        coordinate = input("Give a coordinate (like A1, B2 etc.): ")
    # check if the valid position is empty
    if coordinate.upper().startswith('A'):
        pass
    if coordinate.upper().startswith('B'):
        row += 1
    if coordinate.upper().startswith('C'):
        row += 2
    col += int(coordinate[-1]) - 1
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
