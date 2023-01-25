import math
T = int(input())
for i in range(T):
  x1, y1, r1, x2, y2, r2 = map(int,input().split())
  r = math.sqrt((x1-x2)**2 + (y1-y2)**2) # 원의 방정식, 두 원의 거리
  
  if r == 0 and r1 == r2:	# 두 원이 동심원이고, 반지름이 같을 때 -> 류재명이 있을 수 있는 위치의 개수: 무한대
    print(-1)
  elif abs(r1-r2) == r or r1 + r2 == r:	# 두 원이 내접, 외접할 때
    print(1)
  elif abs(r1-r2) < r < (r1+r2): # 두 원이 서로 다른 두 점에서 만날 때
    print(2)
  else: print(0)
