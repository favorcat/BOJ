import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(x,y,h):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]    
    if 0 <= nx < n and 0 <= ny < n and m[nx][ny] > h and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx,ny,h)

ans = 1
for i in range(max(map(max,m))):
  cnt = 0
  visited = [[False] * n for _ in range(n)]
  for j in range(n):
    for k in range(n):
      if m[j][k] > i and not visited[j][k]:
        visited[j][k] = True
        cnt += 1
        dfs(j,k,i)
  ans = max(ans,cnt)
print(ans)