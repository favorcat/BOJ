import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
p = list(map(int,input().split()))
dq = deque(i for i in range(1,n+1))
cnt = 0

for a in p:
  if a == dq[0]:
    dq.popleft()
  else:
    idx  = dq.index(a)
    right = len(dq) - idx
    left = idx
    if left < right:
      dq.rotate(-left)
      cnt += left
    else:
      dq.rotate(right)
      cnt += right
    dq.popleft()
    
print(cnt)