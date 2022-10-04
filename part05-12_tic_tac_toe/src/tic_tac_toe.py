# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if y < 0 or y > 2 or x > 2 or x < 0:
        return False


    elif game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    return False


