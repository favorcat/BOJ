t = int(input())
for _ in range(t):
  x1,y1,x2,y2 = map(int,input().split())
  n = int(input())
  cnt = 0
  for _ in range(n):
    cx,cy,r = map(int,input().split())
    dis1 = (x1-cx)**2 + (y1-cy)**2
    dis2 = (x2-cx)**2 + (y2-cy)**2
    if dis1 < r**2 and dis2 < r**2:
      pass
    elif dis1 < r**2:
      cnt += 1
    elif dis2 < r**2:
      cnt += 1
  print(cnt)