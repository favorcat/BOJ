import sys
input = sys.stdin.readline
n, k = map(int,input().split())
li = [[0,0]]
for _ in range(n):
  li.append(list(map(int,input().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
  for k in range(1, k+1):
    weight = li[i][0]
    value = li[i][1]
    
    if k < weight:
      dp[i][k] = dp[i-1][k]
    else:
      dp[i][k] = max(value+dp[i-1][k-weight], dp[i-1][k])
print(dp[n][k])