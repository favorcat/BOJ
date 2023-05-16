from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
  m = int(input())
  left = deque(map(int, input().split()))
  right = deque(map(int, input().split()))
  
  ans = 0
  cnt = 0
  while left:
    tmp = left.popleft()
    if tmp + 1000 in right:
      cnt += 1
    if cnt == 2:
      cnt = 0
      ans += 1
  print(ans)