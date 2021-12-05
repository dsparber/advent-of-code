
def won(board):
    for i in range(5):
        row_sum = 0
        col_sum = 0
        for j in range(5):
            row_sum += board[i][j]
            col_sum += board[j][i]

        if row_sum == 0 or col_sum == 0:
            return True

    return False


def mark_number(board, n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                board[i][j] = 0


def board_sum(board):
    return sum([sum(row) for row in board])


def simulate(boards, random_numbers):
    remaining_boards = boards
    for number in random_numbers:
        for board in remaining_boards:
            mark_number(board, number)
            if won(board) and len(remaining_boards) == 1:
                print("number = {}, sum = {}".format(number, board_sum(board)))
                return number * board_sum(board)
        remaining_boards = [b for b in remaining_boards if not won(b)]
    return -1


with open("input", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    random_numbers = [int(x) for x in lines[0].split(",")]

    boards = list()

    for board_start in range(2, len(lines), 6):
        board = [[int(x) for x in line.split()] for line in lines[board_start:(board_start+5)]]
        boards.append(board)

    product = simulate(boards, random_numbers)
    print(product)


