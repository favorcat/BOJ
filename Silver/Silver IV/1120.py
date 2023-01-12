x, y = map(str,input().split())
lx = len(x)
ly = len(y)
res = 50

for i in range(ly-lx+1):
  cnt = 0
  for k in range(lx):
    if x[k] != y[i+k]:
      cnt += 1
  if cnt < res: res = cnt
print(res)
