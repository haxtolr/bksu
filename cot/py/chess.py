ans_wb = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

ans_bw = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], 
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

def check(n, t, answer, board):
    diff_bw = 0
    diff_wb = 0
    
    for i in range(8):
        for j in range(8):
            if diff_bw > answer and diff_wb > answer:
                return(answer)
            if board[n+i][t + j] != ans_wb[i][j]:
                diff_wb += 1
            if board[n+i][t + j] != ans_bw[i][j]:
                diff_bw += 1

    return min(diff_bw, diff_wb)

num = list(map(int, input().split()))
board = [list(input()) for _ in range(num[0])]
row = num[1]
col = num[0]

n = 0
t = 0

max = 0
answer = 10000
for i in range(col - 7):
    for t in range(row - 7):
        answer = min(check(i, t, answer, board), answer)

print(answer)