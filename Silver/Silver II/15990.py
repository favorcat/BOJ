import sys
input = sys.stdin.readline
t = int(input())

dp = [[0,0,0] for _ in range(100001)]
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]
div = 1000000009

for i in range(4, 100001):
  dp[i][0] = dp[i-1][1] % div + dp[i-1][2] % div
  dp[i][1] = dp[i-2][0] % div + dp[i-2][2] % div
  dp[i][2] = dp[i-3][0] % div + dp[i-3][1] % div

for i in range(t):
    n = int(input())
    print(sum(dp[n]) % div)