import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10

for i in range(1, n):
  for k in range(1,10):
    dp[k] += dp[k-1]

print(sum(dp)%10007)
