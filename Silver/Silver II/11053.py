n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
  for k in range(i):
    if a[i] > a[k] and dp[i] < dp[k]:
      dp[i] = dp[k]
  dp[i] += 1

print(max(dp))
