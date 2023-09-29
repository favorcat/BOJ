n, m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
m, k = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(m)]

for i in range(n):
  ans = []
  for j in range(k):
    tmp = 0
    for l in range(m):
      tmp += a[i][l] * b[l][j]
    ans.append(tmp)
  print(*ans)
