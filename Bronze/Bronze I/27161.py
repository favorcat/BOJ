from sys import stdin
n = int(stdin.readline())
idx = 0	# 시간 인덱스
hour_flag = False	# 시간이 역행인지 보는 플래그

for i in range(n):
  # 시계의 종류와 카드에 적힌 시간
  card, clock = map(str, stdin.readline().split())
  clock = int(clock)
  
  # 시간이 역행인지에 따른 시간 인덱스 조정
  if hour_flag: idx -= 1
  else: idx += 1
  
  # 시간은 12시가 최대이므로 넘어가면 다시 조정
  if idx >= 13: idx = 1
  if idx <= 0: idx = 12
  
  # 플레이어가 외칠 시간
  print(idx, end=" ")
  
  # 만약 모래시계를 펼쳤다면
  if card == "HOURGLASS":
  	# 시간 역행 플래그를 반대로 뒤집는다
    hour_flag = not(hour_flag)

  # 만약 플레이어가 외치는 시간과 카드에 적힌 시간이 같다면
  if clock == idx :
  	# 모래시계를 꺼냈을 경우, 과부하의 원칙에 따라 둘 다 무효화가 되어
    # 시간 역행 플래그를 다시 원래대로 돌리고, 게임판을 내리칠 수 없다
    if card == "HOURGLASS":
      answer = False
      hour_flag = not(hour_flag)
      
    # 모래시계를 펼치지 않았을 경우, 게임판을 내리칠 수 있다
    else:
      answer = True

  # 외치는 시간과 카드에 적힌 시간이 다르다면, 게임판을 내리칠 수 없다
  else: answer = False
  
  if answer: print("YES")
  else: print("NO")
