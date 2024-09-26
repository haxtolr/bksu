import sys
input = sys.stdin.readline

def main():
    n = int(input())
    board = [-1] * n
    result = [0]
    back(n , board, 0, result)
    print(result[0])

def back(n, board, row, result):
    if row == n:
        result[0] += 1
        return
    
    for col in range(n):
        if is_ok(board, row, col):
            board[row] = col
            back(n, board ,row + 1, result)
            board[row] = -1

def is_ok(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

main()