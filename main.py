def valid_user(user_name):
    if len(user_name) == 1:
        return True


def user(number):
    u1 = input(f'Player {number} please choose an integer or letter to represent your player: ')
    while not valid_user(u1):
        print('Your username must be 1 character long!')
        u1 = input(f'Player {number} please choose an integer or letter to represent your player: ')
    return u1


def print_board(board, options):
    print('  '.join(options))
    print('\n'.join(map('  '.join, board)))
    print('\n')


def choose_spot(board, letter):
    try:
        s = int(input('Choose your spot: '))
        print('\n')
        x = 6
        while board[x][s - 1] != '*':
            x -= 1
        board[x][s - 1] = letter
        return True
    except IndexError:
        print('That spot is not an option. Try again.')
    except ValueError:
        print('That spot is not an option. Try again.')


def vertical_win(letter, board):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y] == board[x - 2][y] == board[x - 3][y] == letter:
                    return True
                else:
                    continue
            except IndexError:
                continue


def horizontal_win(letter, board):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x][y + 1] == board[x][y + 2] == board[x][y + 3] == letter:
                    return True
                else:
                    continue
            except IndexError:
                continue


def diagonal_win(letter, board):
    for x in range(6, -1, -1):
        for y in range(7):
            try:
                if board[x][y] == board[x - 1][y + 1] == board[x - 2][y + 2] == board[x - 3][y + 3] == letter:
                    return True
                elif board[x][y] == board[x - 1][y - 1] == board[x - 2][y - 2] == board[x - 3][y - 3] == letter:
                    return True
            except IndexError:
                continue


def main():
    turns = 0
    one = user('one')
    two = user('two')
    letter = one
    options = ['1', '2', '3', '4', '5', '6', '7']
    board = [['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*'],
             ['*', '*', '*', '*', '*', '*', '*'], ]
    while True:
        print_board(board, options)
        if vertical_win(letter, board):
            turns -= 1
            print(letter, 'won vertically! Congratulations')
            break
        elif horizontal_win(letter, board):
            turns -= 1
            print(letter, 'won horizontally! Congratulations')
            break
        elif diagonal_win(letter, board):
            turns -= 1
            print(letter, 'won diagonally! Congratulations')
            break
        if turns % 2 == 0:
            letter = one
        else:
            letter = two

        if choose_spot(board, letter):
            turns += 1



if __name__ == "__main__":
    main()
