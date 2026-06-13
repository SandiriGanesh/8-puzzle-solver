def print_board(board):
    for row in board:
        for number in row:
            if number == 0:
                print("_", end=" ")
            else:
                print(number, end=" ")
        print()


def find_blank(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                return (row, col)


def get_possible_moves(board):
    row, col = find_blank(board)

    moves = []

    if row > 0:
        moves.append("up")

    if row < 2:
        moves.append("down")

    if col > 0:
        moves.append("left")

    if col < 2:
        moves.append("right")

    return moves


def move(board, direction):
    row, col = find_blank(board)

    # create a copy of the board
    new_board = [r[:] for r in board]

    if direction == "up":
        new_board[row][col], new_board[row - 1][col] = (
            new_board[row - 1][col],
            new_board[row][col],
        )

    elif direction == "down":
        new_board[row][col], new_board[row + 1][col] = (
            new_board[row + 1][col],
            new_board[row][col],
        )

    elif direction == "left":
        new_board[row][col], new_board[row][col - 1] = (
            new_board[row][col - 1],
            new_board[row][col],
        )

    elif direction == "right":
        new_board[row][col], new_board[row][col + 1] = (
            new_board[row][col + 1],
            new_board[row][col],
        )

    return new_board


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Current Board:\n")
print_board(initial_state)

print("\nBlank Position:", find_blank(initial_state))

print("\nPossible Moves:", get_possible_moves(initial_state))

new_state = move(initial_state, "left")

print("\nBoard After Moving Left:\n")
print_board(new_state)