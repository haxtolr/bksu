import sys

input = sys.stdin.readline

def main():
    n, k = list(map(int, input().split()))

    bc = [list(map(int, input().split())) for _ in range(n)]
    print(dpa(n, k, bc))
def dpa(n, k, bc):
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(k + 1):
            if bc[i - 1][0] <= t:
                dp[i][t] = max(dp[i - 1][t], bc[i- 1][1] + dp[i-1][t-bc[i-1][0]])
            else:
                dp[i][t] = dp[i-1][t]
    return dp[n][k]


main()