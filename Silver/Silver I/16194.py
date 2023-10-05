n = int(input())
p = [0] + list(map(int,input().split()))
dp = [1000001] * (n+1)
dp[0] = 0

for i in range(n+1):
  for j in range(n+1):
    dp[i] = min(dp[i], dp[i-j]+p[j])
print(dp[-1])