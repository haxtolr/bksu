from collections import deque

def sol(board):
    row = len(board)
    col = len(board[0])
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(row):
        for t in range(col):
            if board[i][t] == 'R':
                stx = i
                sty = t
            elif board[i][t] == 'G':
                ex = i
                ey = t
    que = deque([(stx, sty, 0)])
    visited = set([stx, sty])

    while que:
        x, y, dist = que.popleft()

        if (x, y) == (ex, ey):
            return dist
        
        for i in moves:
            nx, ny = x + i[0], y + i[1]

            while 0 <= nx < row and 0 <= ny < col and board[nx][ny] != "D":
                nx += i[0]
                ny += i[1]
            
            nx -= i[0]
            ny -= i[1]

            if (nx, ny) not in visited:
                que.append((nx, ny, dist + 1))
                visited.add((nx, ny))
            
    return -1
            

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(sol(board))