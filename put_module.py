def game_put(game, row_num, col_num, curent_player):
    if game[row_num][col_num] == "-":
        game[row_num][col_num] = curent_player
        print(f"Player '{curent_player}' your turn is done..:)")
        return True
    else:
        return False

# def put(game, row, col, player):

# 	if game[row][col] == ' ':
# 		game{row}{col} = player

# 		return True
# 	else:
# 		return False

# if __name__ == '__main__':
# 	game = [
#          [' ', ' ', ' '],
#          [' ', ' ', ' '],
#          [' ', ' ', ' ']
#      ]

#      player= 'X'
# 	 put(game, 0, 0, player)
# 	 for i in range(3):
# 	 	print(game[i])
