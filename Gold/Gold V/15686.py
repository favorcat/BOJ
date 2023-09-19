import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1: house.append((i, j))
    elif city[i][j] == 2: chicken.append((i, j))

ans = 1e9
for chick in combinations(chicken, m):
  tmp = 0
  for hx, hy in house:
    tmp2 = 1e9
    for cx, cy in chick:
      tmp2 = min(tmp2, abs(hx - cx) + abs(hy - cy))
    tmp += tmp2
  ans = min(ans, tmp)
print(ans)