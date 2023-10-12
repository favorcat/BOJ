from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = [[-1] * m for _ in range(n)]
queue = deque([])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(n):
  for j in range(m):
    if li[i][j] == 2:
      queue.append((i,j))
      visited[i][j] = True
      ans[i][j] = 0
    if li[i][j] == 0:
      ans[i][j] = 0

while queue:
  x, y = queue.popleft()
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and li[nx][ny] == 1:
      queue.append((nx,ny))
      visited[nx][ny] = True
      ans[nx][ny] = ans[x][y] + 1

for i in range(n):
  for j in range(m):

    print(ans[i][j],end=' ')
  print()