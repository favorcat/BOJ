n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if i == n - 1 and j == n - 1:
      print(dp[i][j])
      break
    if j + a[i][j] < n:
      dp[i][j + a[i][j]] += dp[i][j]
    if i + a[i][j] < n:
      dp[i + a[i][j]][j] += dp[i][j]