n = int(input())
a = list(map(int, input().split()))
dp = a[:]

for i in range(n):
  for k in range(i):
    if a[i] > a[k]:
      dp[i] = max(dp[i], dp[k]+a[i])

print(max(dp))
