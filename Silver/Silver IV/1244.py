import sys
input = sys.stdin.readline
n = int(input())
switch = list(map(int,input().split()))

m = int(input())
for _ in range(m):
  a, b = map(int,input().split())
  if a == 1: # 남자
    for i in range(b-1, n, b):
      if switch[i] == 1: switch[i] = 0
      else: switch[i] = 1
  elif a == 2: #여자
    if switch[b-1] == 1: switch[b-1] = 0
    else: switch[b-1] = 1
    left = b-2
    right = b
    while left >= 0 and right < n:
      if switch[left] == switch[right]:
        if switch[left] == 1:
          switch[left] = 0
          switch[right] = 0
        else:
          switch[left] = 1
          switch[right] = 1
        left -= 1
        right += 1
      else: break

cnt = 0
for i in range(n):
  print(switch[i], end=" ")
  cnt += 1
  if cnt % 20 == 0: print()