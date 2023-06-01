from collections import deque
import sys
input = sys.stdin.readline

a, b = map(int,input().split())
n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
  x, y = map(int,input().split())
  graph[x].append(y)
  graph[y].append(x)

def bfs():
  q = deque([a])
  visited[a] = 1
  while q:
    p = q.popleft()
    if visited[b]:
      return visited[b] - 1
    for i in graph[p]:
      if not visited[i]:
        visited[i] = visited[p] + 1
        q.append(i)
  return -1

print(bfs())