n, m = map(int,input().split())
r, c, d = map(int,input().split())
room = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
ans = 0

def clean(x, y, d):
  global ans
  if not room[x][y]:
    room[x][y] = 2
    ans += 1
  for _ in range(4):
    nd = (d+3)%4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if not room[nx][ny]:
      clean(nx, ny, nd)
      return
    d = nd
  nd = (d+2)%4
  nx = x + dx[nd]
  ny = y + dy[nd]
  if room[nx][ny] == 1:
    return
  clean(nx, ny, d)
clean(r,c,d)
print(ans)