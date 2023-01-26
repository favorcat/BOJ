n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n-1, -1, -1): # n-1부터 거꾸로 계산
  if i + arr[i][0] > n: # 현재 날짜+상담을 완료하는데 걸리는 기간이 퇴사일보다 크면
    dp[i]=dp[i+1] # i번째 일을 건너뛰고 i+1번째 일을 할 때의 이익
  else:
  	# dp[i]는 i번째 날의 수익과 i번째 일을 하는데 걸리는 시간 후의 이익을 더한 값과,
    # i번째 일을 건너뛰고 i+1번째 일을 할 때의 이익 중 최대를 넣어준다 
    dp[i]=max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

print(dp[0])
