n, m = map(int, input().split())
a = []
b = []

for _ in range(n):
  a.append(list(map(int,input().split())))
for _ in range(n):
  b.append(list(map(int,input().split())))

for i in range(n):
  s = []
  for k in range(m):
    s.append(a[i][k]+b[i][k])
  print(" ".join(map(str,s)))
