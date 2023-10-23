from collections import deque
import sys
input = sys.stdin.readline
f,s,g,u,d = map(int,input().split())

def bfs(x):
  q = deque([])
  q.append((x, 0))
  visited = [0]*(f+1)
  visited[x] = 1
  while q:
    ans, cnt = q.popleft()
    if ans == g:
      return cnt
    for i in ('u', 'd'):
      nx = ans + u if i == 'u' else ans - d
      if 0<nx<=f and visited[nx] == 0:
        q.append((nx, cnt+1))
        visited[nx] = 1
  return "use the stairs"
print(bfs(s))