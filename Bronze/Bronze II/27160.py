n = int(input())
card = {}

# 과일의 종류와 과일의 개수를 n줄에 걸쳐서 입력받아 card에 저장
for _ in range(n):
  a,b = map(str, input().split())
  if a not in card:
    card[a] = int(b)
  else:
    card[a] += int(b)

flag = False	# 종을 쳐야하는지 보는 플래그
for key, value in card.items():
  if value == 5:	# 만약 과일의 수가 5인 요소가 있다면
    flag = True
if flag: print("YES")
else: print("NO")
