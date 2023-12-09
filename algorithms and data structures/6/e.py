board = [[0 for _ in range(10)] for _ in range(10)]

x, y = map(int, input().split())

def update_board(x, y, init=False):
    board[x][y] = board[x + 1][y - 1] + board[x + 1][y + 1]
    if init:
        board[x][y] = 1
    if x - 1 != 0:
        if y + 1 != 9:
            update_board(x - 1, y + 1)
        if y - 1 != 0:
            update_board(x - 1, y - 1)

update_board(9-y, x, init=True)
#print(*board, sep="\n")
print(sum(board[1]))