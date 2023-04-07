from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [False] * (n+1)
m = [[] for _ in range(n+1)]
res = [0] * (n+1)

for i in range(n-1):
  a, b = map(int,input().split())
  m[a].append(b)
  m[b].append(a)

def bfs (m, v, visited):
  q = deque([v])
  visited[v] = True
  while q:
    x = q.popleft()
    for i in m[x]:
      if not visited[i]:
        q.append(i)
        visited[i] = True
        res[i] = x
bfs(m, 1, visited)

for i in range(2, n+1):
  print(res[i])