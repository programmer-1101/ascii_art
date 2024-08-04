class Colors:
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


class Piece:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        return self.name


def print_chess_board(chess_board, highlight=None):
    if highlight is None:
        highlight = []
    for row in range(8):
        for col in range(8):
            color = Colors.WHITE
            piece = chess_board[row][col]
            if [row, col] in highlight:
                color = Colors.RED
            elif piece.colour == "black":
                color = Colors.GREEN
            elif piece.colour == "white":
                color = Colors.WHITE
            print(f"{color}{piece}{Colors.RESET} ", end="")
        print()


def ask_user_input():
    while True:
        try:
            row = int(input("Enter row (1-8):")) - 1
            column = int(input("Enter column (1-8):")) - 1
            if 0 <= row <= 7 and 0 <= column <= 7:
                return row, column
            else:
                print("Invalid input. Row and column must be between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")


def print_possible_moves(board, x1, x2, turn):
    return_value = []
    piece = board[x1][x2]

    if turn == (piece.colour == 'white'):
        direction = 1 if turn else -1
        initial_row = 1 if turn else 6
        opponent_color = 'black' if turn else 'white'

        if piece.name == 'p':
            if board[x1 + direction][x2].name == '_':
                return_value.append([x1 + direction, x2])
                if x1 == initial_row and board[x1 + 2 * direction][x2].name == '_':
                    return_value.append([x1 + 2 * direction, x2])
            for dx in [-1, 1]:
                if 0 <= x2 + dx < 8 and board[x1 + direction][x2 + dx].colour == opponent_color:
                    return_value.append([x1 + direction, x2 + dx])

        elif piece.name == 'N':
            possible_moves = [(x1 + 2, x2 + 1), (x1 + 2, x2 - 1), (x1 + 1, x2 + 2), (x1 + 1, x2 - 2),
                              (x1 - 2, x2 + 1), (x1 - 2, x2 - 1), (x1 - 1, x2 + 2), (x1 - 1, x2 - 2)]
            for move in possible_moves:
                nx, ny = move
                if 0 <= nx < 8 and 0 <= ny < 8 and (board[nx][ny].colour == opponent_color or board[nx][ny].name == '_'):
                    return_value.append([nx, ny])

        elif piece.name == 'B':
            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                end = False
                y = 1
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1

        elif piece.name == 'R':
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                y = 1
                end = False
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1

        elif piece.name == 'Q':
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                y = 1
                end = False
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1

            for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                end = False
                y = 1
                while not end:
                    nx = x1 + y * dx
                    ny = x2 + y * dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_':
                            return_value.append([nx, ny])
                        elif board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])
                            end = True
                        else:
                            end = True
                    else:
                        end = True
                    y += 1

        elif piece.name == 'K':
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx = x1 + dx
                    ny = x2 + dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        if board[nx][ny].name == '_' or board[nx][ny].colour == opponent_color:
                            return_value.append([nx, ny])

    else:
        print("Wrong Turn")

    if not return_value:
        print("No moves available")

    return return_value


def ask_move(board, possible_moves, row, column):
    while True:
        input_string = input("Enter move (e.g., '3 4'): ")
        try:
            move = [int(x) - 1 for x in input_string.split()]
            if len(move) == 2 and move in possible_moves:
                initial_piece = board[row][column]
                board[move[0]][move[1]] = initial_piece
                board[row][column] = Piece('_', 'normal')
                return
            else:
                print("Invalid move. Please enter a valid move from the list of possible moves.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter integers between 1 and 8 for both row and column.")


def main():
    end = False
    turn = True

    chess_board = [
        [Piece('R', 'white'), Piece('N', 'white'), Piece('B', 'white'), Piece('K', 'white'), Piece('Q', 'white'),
         Piece('B', 'white'), Piece('N', 'white'), Piece('R', 'white')],
        [Piece('p', 'white')] * 8,
        [Piece('_', 'normal')] * 8,
        [Piece('_', 'normal')] * 8,
        [Piece('_', 'normal')] * 8,
        [Piece('_', 'normal')] * 8,
        [Piece('p', 'black')] * 8,
        [Piece('R', 'black'), Piece('N', 'black'), Piece('B', 'black'), Piece('K', 'black'), Piece('Q', 'black'),
         Piece('B', 'black'), Piece('N', 'black'), Piece('R', 'black')]
    ]

    while not end:
        print_chess_board(chess_board)

        print("Whites Turn" if turn else "Blacks Turn")

        possible_moves = []
        row, column = 0, 0

        while True:
            row, column = ask_user_input()
            possible_moves = print_possible_moves(chess_board, row, column, turn)
            if possible_moves:
                break
            print("No moves found")

        print_chess_board(chess_board, possible_moves)
        print("Possible moves:", possible_moves)
        ask_move(chess_board, possible_moves, row, column)
        turn = not turn


if __name__ == "__main__":
    main()
