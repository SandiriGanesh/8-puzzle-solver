from collections import deque


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

    new_board = [r[:] for r in board]

    if direction == "up":
        new_board[row][col], new_board[row - 1][col] = (
            new_board[row - 1][col],
            new_board[row][col]
        )

    elif direction == "down":
        new_board[row][col], new_board[row + 1][col] = (
            new_board[row + 1][col],
            new_board[row][col]
        )

    elif direction == "left":
        new_board[row][col], new_board[row][col - 1] = (
            new_board[row][col - 1],
            new_board[row][col]
        )

    elif direction == "right":
        new_board[row][col], new_board[row][col + 1] = (
            new_board[row][col + 1],
            new_board[row][col]
        )

    return new_board


def get_children(board):
    children = []

    for move_direction in get_possible_moves(board):
        child = move(board, move_direction)
        children.append(child)

    return children


def board_to_tuple(board):
    return tuple(tuple(row) for row in board)


def is_goal(board, goal):
    return board == goal


def bfs(start_board, goal_board):
    queue = deque()
    visited = set()
    parents = {}

    start_key = board_to_tuple(start_board)

    queue.append(start_board)
    visited.add(start_key)

    parents[start_key] = None

    while queue:

        current_board = queue.popleft()

        if is_goal(current_board, goal_board):

            print("\nGoal Found!")

            path = []

            current_key = board_to_tuple(current_board)

            while current_key is not None:
                board = [list(row) for row in current_key]
                path.append(board)
                current_key = parents[current_key]

            path.reverse()

            print("\nSolution Path:\n")

            for step, board in enumerate(path):
                print(f"Step {step}:")
                print_board(board)
                print()

            print("Total Moves:", len(path) - 1)

            return True

        children = get_children(current_board)

        for child in children:

            child_key = board_to_tuple(child)

            if child_key not in visited:

                visited.add(child_key)

                parents[child_key] = board_to_tuple(current_board)

                queue.append(child)

    print("\nNo Solution Found!")

    return False


initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

print("Initial Board:\n")
print_board(initial_state)

print("\nStarting BFS Search...")

bfs(initial_state, goal_state)