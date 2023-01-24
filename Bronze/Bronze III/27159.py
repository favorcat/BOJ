# 카드의 개수
n = int(input())

# N개의 카드
card = list(map(int, input().split()))
card.sort() # 카드 오름차순 정렬

answer = 0 		# 정답(점수)
arr = [card[0]] # 그룹화하여 담을 리스트
tmp = card[0] 	# 연속하는 수 인지 판별하기 위한 변수

for i in range(n):
  if i > 0:
    if card[i]-tmp != 1: # 만약 이전의 수와 차가 1이 아니라면
      answer += arr[0] 	 # 점수에 그룹의 가장 작은 수를 더하고
      arr = []			 # 그룹을 초기화
    tmp = card[i]		 # 현재 수를 tmp에 담고
    arr.append(card[i])	 # 그룹에 현재 수를 추가

  if i == n-1:			 # 마지막 요소라면
    answer += arr[0]	 # 현재 그룹의 가장 작은 수를 더함

print(answer)
