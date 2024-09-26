from collections import deque

def solution(tickets):
    answer = []
    
    def dfs():
        que = deque(["ICN"])
        ans = []
        while que:
            now = que.popleft()
            v = []
            for i, t in tickets:
                if i == now:
                    v.append(t)
                v.sort()
                if len(v) > 0:
                    t = v[0]
                    que.append(t)
                    if [now, t] in tickets:
                        tickets.remove([now, t])
            ans.append(now)
        return ans
    
    answer = dfs()
    return answer

solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])