n = int(input())
n2 = int(input())
ans = [[0 for _ in range(n)] for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = n//2, n//2
ans[x][y] = 1
num = 2
tx, ty = 0, 0
if n2 == 1:
  tx, ty = n//2+1, n//2+1

for i in range(1, n//2+1):
  if num == 2:
    nx, ny = x-1, y-1
  else:
    nx, ny = nx-1, ny-1
  
  step = i*2
  for j in range(4):
    for k in range(step):
      nx+=dx[j]
      ny+=dy[j]
      ans[nx][ny] = num
      if num == n2:
        tx, ty = nx+1, ny+1
      num+=1

for i in range(n):
  print(*ans[i])
print(tx,ty)