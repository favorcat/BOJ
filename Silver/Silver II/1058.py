import sys
input = sys.stdin.readline
n = int(input())
m = [list(input()) for _ in range(n)]
li = [[0]*n for _ in range(n)]

for i in range(n):
  for k in range(n):
    for j in range(n):
      if k == j:
        continue
      if m[k][j] == "Y" or (m[k][i] == "Y" and m[i][j] == "Y"):
        li[k][j] = 1

res = 0
for i in li:
  res = max(res, sum(i))
print(res)