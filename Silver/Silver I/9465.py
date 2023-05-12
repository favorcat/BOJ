import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  
  dp = [[0]*3 for _ in range(n)]
  dp[0][0] = a[0]
  dp[0][1] = b[0]
  dp[0][2] = 0
  
  for i in range(1, n):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1])
    
  print(max(dp[n-1]))
