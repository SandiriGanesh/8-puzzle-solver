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


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

print("Current Board:\n")
print_board(initial_state)

blank_position = find_blank(initial_state)

print("\nBlank Position:", blank_position)