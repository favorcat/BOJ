c,r = map(int,input().split())
k = int(input())

dx = [0,1,0,-1]
dy = [-1,0,1,0]

if k > c*r :
  print(0)
  exit()

grid = [[0]*c for _ in range(r)]
next = x = y = 0

for seat in range(1,c*r+1) :
  if seat == k:
    print(y+1,x+1)
    break
  else :
    grid[x][y] = seat
    x += dx[next]
    y += dy[next]
    if x<0 or y<0 or x>=r or y>=c or grid[x][y]:
      x -= dx[next]
      y -= dy[next]
      next = (next+1)%4
      x += dx[next]
      y += dy[next]