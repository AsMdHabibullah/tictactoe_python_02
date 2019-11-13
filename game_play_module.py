from next_player_module import next_player
# from game_print import game_print
from print_game_module import print_game

from put_module import game_put

print("# Global Variable")
print("-"*20)

game_still_goinon = False
# valid = True


def play_game(game, curent_player):

    # if variable decliers in global then for calling purpose we must need to add global key first
    global game_still_goinon, valid

    # multi input from users
    while not game_still_goinon:

        row = input('row ')
        col = input('col ')

        row = row.strip()
        col = col.strip()
        row_num = int(row)
        col_num = int(col)

        nxt_player = next_player(curent_player)

        if game[row_num][col_num] != "-":
            print(
                f"You can't choose ({row_num, col_num}) row & column. Please choose anothe one..:)")
        else:
            success = game_put(game, row_num, col_num, curent_player)

            if success:
                print_game(game_bord)
                print("Player '" + nxt_player + "' right now your turn..!")
                play_game(game, nxt_player)


if __name__ == "__main__":

    game_bord = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]

    player = 'X'
    print("Default player '" + player + "' your turn..!")
    play_game(game_bord, player)
