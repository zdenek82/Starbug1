import random

def main():
    print_intro()
    board, player = setup_game()
    while True:
        print_board(board)
        board = make_move(player, board)
        if check_game_over(board, player):
            print_game_over(player)
            break
        elif board_full(board):
            print_tie()
            break
        player = swap_players(player)
    print_board(board)


#######################
def setup_game():
    size = int(input('Please enter the board size: '))
    board = []
    for row in range(size):
        board.append([' '] * size)
    player_to_start = random.choice(['x', 'o'])
    return board, player_to_start


#######################
def print_intro():
    print('''
    ===========================
    Welcome to Tic Tac Toe
    GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    Let's start the game
''', end='\n\n\n')

def print_board(board):
    b = []
    size = len(board)
    b.append('\n' + '-' * size * 2 + '\n')
    for row in board:
        b.append('|'.join(row) + '\n')
        b.append('-' * size * 2 + '\n')
    print(''.join(b))


#######################
def make_move(player, board):
    while True:
        move = int(input('Player {} | Please enter your move number:'.format(player)))
        row, col = to_coord(move, len(board))
        if board[row][col] == ' ':
            board[row][col] = player
            break
            print('\nThis position is already taken\n')
    return board


# Pomocna funkce pro tah
def to_coord(scalar_pos, size):
    # Ziskani souradnice slopce ze skalaru
    column = (scalar_pos - 1) % size

    # Ziskani souradnice radku ze skalaru
    row = round((scalar_pos - column) // size)

    # Vracenime radek a sloupec
    return row, column


#######################
# Tah druheho hrace
def swap_players(player):
    # Vraceni opacneho symbolu
    return 'x' if player == 'o' else 'o'


#######################
# Ukonceni hry - Vyhra/Prohra
def check_game_over(board, player):
    # Velikost hraci plochy
    size = len(board)

    # Prevod na 1-dimensionalni list
    flat_board = flatten(board)

    # Prochazime kazdou radu
    for i in range(size):

        # Kontrola radku a sloupcu
        if set(flat_board[i * size:i * size + size]) == set(player) \
                or set(flat_board[i:size ** 2:size]) == set(player):
            return True  # row & column

        # Kontrola diagonaly zleva dolu
        if i == 0 and set(flat_board[i:size ** 2:size + 1]) == set(player):
            return True

        # Kontrola diagonaly zprava dolu
        elif i == size - 1 and set(flat_board[i:size ** 2 - 1:size - 1]) == set(player):
            return True


# Pomocna funkce pro ukonceni hry
def flatten(board):
    # Pomocna promenna pro 1-dimensionalni list
    flat = []

    # Secti jednotlive radky board do flat
    for row in board:
        flat += row

    # Vrat 1-dimensionalni list
    return flat


# Funkce pro tisk vyherce
def print_game_over(player):
    # Oddelovac
    print('\n{}\n'.format('=' * 20))

    # Vyherce
    print('Congratulations, the player {} WON!'.format(player))


#######################
# Ukonceni hry - Remiza
def board_full(board):
    # Je nejake volne misto v board?
    return ' ' not in flatten(board)


# Funkce pro tisk remízy
def print_tie():
    # Oddelovac
    print('\n{}\n'.format('=' * 20))

    # Remiza
    print('Nobody wins, this is a tie')


main()