number_of_sticks = 10
player_turn = 1


def can_take(sticks):
    return 1 <= sticks <= 3 


def switch_player_turn(turn):
    return 1 if turn==2 else 2


def end_of_game(sticks):
    return sticks <= 0


while not end_of_game(number_of_sticks):
    print(f'How many sticks your take ? Remaining {number_of_sticks}')
    taken = int(input())

    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks.')
        continue

    
    number_of_sticks -= taken 
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost!')
        break

    player_turn = switch_player_turn(player_turn)