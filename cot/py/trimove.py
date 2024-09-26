def solution(n):
    answer = -1
    sol=[]
    for i in range(1, n+1):
        sol.append([i])
    t = 0
    for i in range(n):
        while len(sol[i]) != i + 1:
            if i == n - 1:
                sol[i].append(n + 1 + t)
                t += 1
            else:
                sol[i].append(0)
    t = 2
    i = 1
    num = sol[n-1][n-1] + 1
    move = 'u'
    print(sol[n-t])
    while 0 not in sol:
        if move == 'u':
            while 0 not in sol[n - t]:
                if sol[n-t][-i] == 0:
                    sol[n-t][-i] = num
                    num += 1
                    t += 1
                if t == n:
                    break
            move = 'd'
            t -= 1
            
        elif move == 'd':
            while 0 not in sol[n-t]:
                if sol[n-t][i] == 0:
                    sol[n-t][i] = num
                    num += 1
                t -= 1
                if t == 0:
                    break
            t += 1
            move = 'r'
        elif move == 'r':
            while 0 not in sol[n-t] and i == len(sol[n-t]):
                if sol[n-t][i] == 0:
                    sol[n-t][i] = num
                    num += 1
                else:
                    i += 1
                if t == n:
                    break
            i -= 1
            t -= 1
            move= 'u'    
    return answer

print(solution(6))