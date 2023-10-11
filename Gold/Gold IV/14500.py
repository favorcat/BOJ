n, m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0

def dfs(x,y,cnt,depth):
  global ans
  if depth == 3:
    ans = max(ans,cnt)
    return
  else:
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
        continue
      
      if depth == 1:
        visited[nx][ny] = True
        dfs(x,y,cnt+li[nx][ny],depth+1)
        visited[nx][ny] = False
      
      visited[nx][ny] = True
      dfs(nx,ny,cnt+li[nx][ny],depth+1)
      visited[nx][ny] = False

for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i,j,li[i][j],0)
    visited[i][j] = False
print(ans)