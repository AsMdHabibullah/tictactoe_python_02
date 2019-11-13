# from print_game_module import print_game
# from next_player_module import next_player
# from put_module import put
# from play_module import play
# # the main function
# def main():

#     # define the blank game
#     game = [
#         [' ', ' ', ' '],
#         [' ', ' ', ' '],
#         [' ', ' ', ' ']
#     ]

#     # print the game for the first time
#     print_game(game)

#     # define player X and O
#     player_x = 'X'
#     player_o = 'O'

#     # set player to player_x at the beginning
#     player = player_x

#     # you know the game can only put 9 chess chess pieces
#     for i in range(9):
#         print(f"It's player {player} turn:")

#         # play one turn
#         play(game, player)

#         # print new game
#         print_game(game)

#         # change player
#         player = next_player(player)
#     pass

# if __name__ == '__main__':
#     main()
