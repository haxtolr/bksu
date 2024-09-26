def solution(n, results):
    answer = 0
    res = set(map(tuple, results))
    
    added = True
    while added:
        added = False
        new_res = set()
        for w, l in res:
            for rw, rl in res:
                if w == rl:
                    if (rw, l) not in res:
                        new_res.add((rw, l))
                        added = True
                if l == rw:
                    if (w, rl) not in res:
                        new_res.add((w, rl))
                        added = True
        res.update(new_res)
        
    for i in range(1, n + 1):
        win_c = sum(1 for win, lose in res if win == i)
        lose_c = sum(1 for win, lose in res if lose == i)
        if win_c + lose_c == n - 1:
            answer += 1
    
    return answer


print(solution(5, [[1, 2], [4, 5], [3, 4], [2, 3]]), 5)