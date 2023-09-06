import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input())
m = [list(input().rstrip()) for _ in range(n)]
ans = 0
ans2 = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]

def dfs(x, y):
  visited[x][y] = 1
  color = m[x][y]
  
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if visited[nx][ny] == 0:
        if m[nx][ny] == color:
          dfs(nx, ny)

for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      dfs(i,j)
      ans += 1

for i in range(n):
  for j in range(n):
    if m[i][j] == 'R':
      m[i][j] = 'G'
visited = [[0]*n for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      dfs(i,j)
      ans2 += 1

print(ans, ans2)