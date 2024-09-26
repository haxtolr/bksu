import sys
input = sys.stdin.readline

def main():
    num = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * num  

    for i in range(1, num):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

main()
