n = int(input())
glass = [0] * 10000	# 포도주가 3잔 이하일 수 있으니 최대 포도주 잔의 개수만큼 리스트 생성
for i in range(n):
  glass[i] = int(input())

dp = [0] * 10000 # dp도 glass의 길이만큼 생성
dp[0] = glass[0]
dp[1] = glass[0] + glass[1]

# 현재와 전전 vs 현재와 이전 vs 현재 잔을 마시지 않는다
dp[2] = max(glass[0] + glass[2], glass[1] + glass[2], dp[1])

for i in range(3, n):
  # 현재와 전전 vs 현재와 이전 vs 현재 잔을 마시지 않는다
  dp[i] = max(glass[i]+dp[i-2], glass[i]+glass[i-1]+dp[i-3], dp[i-1])

print(max(dp))
