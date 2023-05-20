from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
com = [combinations(arr, i) for i in range(1, n+1)]
ans = 1000000000

for food in com:
  for a in food:
    s = 1
    b = 0
    for k in a:
      s *= k[0]
      b += k[1]
    ans = min(ans, abs(s - b))
print(ans)
