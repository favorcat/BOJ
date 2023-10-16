n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
for i in range(n):
  for j in range(coin[i],k+1):
    if j == coin[i]:
      dp[j] += 1
    else:
      dp[j] += dp[j-coin[i]]
print(dp[k])