def print_game(game):
    print('  {}     {}     {}  '.format('0', '1', '2'))
    print('0 {}  |  {}  |  {}  '.format(game[0][0], game[0][1], game[0][2]))
    print(' --- --- --- --- ')
    print('1 {}  |  {}  |  {}  '.format(game[1][0], game[1][1], game[1][2]))
    print(' --- --- --- --- ')
    print('2 {}  |  {}  |  {}  '.format(game[2][0], game[2][1], game[2][2]))
    print()


# if __name__== '__main__':

#     game = [
#          [' ', ' ', ' '],
#          [' ', 'X', ' '],
#          [' ', ' ', 'O']
#      ]

#     print_game(game)
