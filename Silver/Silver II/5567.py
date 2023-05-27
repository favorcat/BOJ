from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[0] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(x):
  visited[x] = 1
  q = deque()
  q.append(x)
  while q:
    a = q.popleft()
    for i in graph[a]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = visited[a] + 1
bfs(1)

cnt = 0
for i in range(2,n+1):
  if visited[i] < 4 and visited[i] != 0:
    cnt += 1
print(cnt)