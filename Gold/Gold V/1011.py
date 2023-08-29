import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  x, y = map(int,input().split())
  d = y - x
  k = 0
  
  while True:
    if d <= k*(k+1):
      break
    k += 1
  if d <= k**2:
    print(k*2-1)
  else:
    print(k*2)