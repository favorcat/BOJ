from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
q = deque()
q.append(n)

visited = [-1 for _ in range(100001)]
visited[n] = 0

while q:
  a = q.popleft()
  if a == k:
    print(visited[a])
    break
  if 0 <= a-1 < 100001 and visited[a-1] == -1:
    visited[a-1] = visited[a] + 1
    q.append(a-1)
  if 0 <= a*2 < 100001 and visited[a*2] == -1:
    visited[a*2] = visited[a]
    q.appendleft(a*2)
  if 0 <= a+1 < 100001 and visited[a+1] == -1:
    visited[a+1] = visited[a] + 1
    q.append(a+1)
