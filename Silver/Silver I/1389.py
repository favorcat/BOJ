import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
res = []

for _ in range(m):
  a,b = map(int,input().split())
  arr[a].append(b)
  arr[b].append(a)

def bfs(v):
  q = deque([v])
  visited[v] = 1
  while q:
    ptr = q.popleft()
    for i in arr[ptr]:
      if not visited[i]:
        q.append(i)
        visited[i] = visited[ptr] + 1

for i in range(1,n+1):
  visited = [0] * (n+1)
  bfs(i)
  res.append(sum(visited))
print(res.index(min(res))+1)