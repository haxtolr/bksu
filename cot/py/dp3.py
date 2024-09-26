import sys

input = sys.stdin.readline

def main():
    test = int(input())

    for _ in range(test):
        n = int(input())
        num = []
        num.append(list(map(int, input().split())))
        num.append(list(map(int, input().split())))
        print(dpa(n, num))


def dpa(n, num):
    
    if n == 1:
        return(max(num[0][0], num[1][0]))
    
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = num[0][0]
    dp[1][0] = num[1][0]
    dp[0][1] = dp[1][0] + num[0][1]
    dp[1][1] = dp[0][0] + num[1][1]
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i - 2]) + dp[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i - 2]) + dp[1][i]
    
    return(max(dp[0][n-1], dp[1][n-1]))
            
main()