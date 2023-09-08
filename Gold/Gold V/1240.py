from collections import deque

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b, c = map(int,input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])

def bfs(start, end):
  queue = deque()
  queue.append((start, 0))
  visited = [False] * (n+1)
  visited[start] = True
  while queue:
    v, d = queue.popleft()
    if v == end: return d
    for i, l in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append((i, d+l))

for _ in range(m):
  a, b = map(int,input().split())
  print(bfs(a,b))