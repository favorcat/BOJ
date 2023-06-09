from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
computer = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int,input().split())
  computer[b].append(a)

def bfs(x):
  q = deque([x])
  cnt = 1
  visited = [False] * (n+1)
  visited[x] = True
  while q:
    p = q.popleft()
    for i in computer[p]:
      if not visited[i]:
        visited[i] = True
        q.append(i)
        cnt += 1
  return cnt

ans = []
for i in range(1, n+1):
  ans.append(bfs(i))

for i in range(len(ans)):
  if max(ans) == ans[i]:
    print(i+1, end=' ')