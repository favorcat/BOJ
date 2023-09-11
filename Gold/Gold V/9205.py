from collections import deque
import sys
input = sys.stdin.readline

def bfs():
  q = deque()
  q.append((x1,y1))
  while q:
    x, y = q.popleft()
    if abs(x-x2) + abs(y-y2) <= 1000:
      print('happy')
      return
    for i in range(n):
      if not visited[i]:
        nx, ny = graph[i]
        if abs(x-nx) + abs(y-ny) <= 1000:
          visited[i] = 1
          q.append((nx,ny))
  print('sad')
  return

t = int(input())
for _ in range(t):
  n = int(input())
  graph = []
  x1, y1 = map(int,input().split())
  for _ in range(n):
    a, b = map(int,input().split())
    graph.append((a, b))
  x2, y2 = map(int,input().split())
  visited = [0 for _ in range(n+1)]
  bfs()