# globals
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

is_win = 0
player = 1


def draw_board():
    for row in board:
        print('  |  '.join(map(str, row)))


def mark():
    return 'X' if player == 1 else 'O'


def place_mark():
    print(f"Player {player}'s Chance.")
    x, y = list(
        map(int, input("Enter row and column numbers to fix spot: ").split()))

    while (x not in range(3) or y not in range(3)):
        x, y = list(
            map(int, input("Enter row and column numbers to fix spot: ").split()))

    if board[x][y] == '-':
        board[x][y] = mark()
    else:
        print("That Spot is taken. Please choose another spot!")
        draw_board()
        place_mark()


def win_indexes(n):

    for i in range(n):
        yield [(i, j) for j in range(n)]

    for j in range(n):
        yield [(i, j) for i in range(n)]

    yield [(i, i) for i in range(n)]

    yield [(i, n - 1 - i) for i in range(n)]


def is_tie():
    if not any('-' in row for row in board):
        return True
    else:
        return False


def is_winner():
    n = len(board)
    for indexes in win_indexes(n):
        if all(board[r][c] == mark() for r, c in indexes):
            return True
    return False


while(is_win == 0):
    draw_board()
    place_mark()
    if(is_winner()):
        print(f'Player {player} wins!')
        draw_board()
        break
    elif(is_tie()):
        print("Tie!")
        draw_board()
        break
    player = (player % 2)+1