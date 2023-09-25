n,m = map(int,input().split())
a = [list(input()) for _ in range(n)]
x,y = 0,0

for i in range(n):
  if 'X' not in a[i]:
    x += 1
for k in range(m):
  if 'X' not in [a[i][k] for i in range(n)]:
    y += 1

print(max(x,y))