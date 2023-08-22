import sys
input = sys.stdin.readline
from collections import defaultdict

while True:
  n, m = map(int,input().split())
  if n == 0 and m == 0:
    break
  
  cd = defaultdict(bool)
  ans = 0
  for _ in range(n):
    cd[int(input())] = True
  for _ in range(m):
    if cd[int(input())]:
      ans += 1
  print(ans)