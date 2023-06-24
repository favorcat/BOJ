from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,input().split()))
per = permutations(a)
ans = 0

for p in per:
  tmp = 0
  for i in range(len(p)-1):
    tmp += abs(p[i]-p[i+1])
  if tmp > ans:
    ans = tmp
print(ans)