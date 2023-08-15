board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_state(state):
    for i, c in enumerate(state):
        if (i+1)%3==0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')

win_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def get_winner(state, combinatios):
    for (x,y,z) in combinatios:
        if state[x] == state[y] and state[y] == state[z] and (state[x]=='X' or state[x]=='O'):
            return state[x]
    return ''

def play_game(board):
    curred_sing = 'x'
    while(get_winner(board, win_combinations) == ''):
        index = int(input(f'Where do you want to draw {curred_sing}?'))
        board[index] = curred_sing

        winner_sing = get_winner(board, win_combinations)
        if winner_sing != '':
            print(f'We have a winner:{winner_sing}')
        curred_sing = 'X' if curred_sing == 'O' else 'O'

print(play_game())