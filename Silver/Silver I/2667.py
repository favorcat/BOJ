from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs(graph, x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  queue = deque()
  queue.append((x, y))
  graph[x][y] = 0
  cnt = 1
  
  while queue:
    a, b = queue.popleft()
    for i in range(4):
      nx = a + dx[i]
      ny = b + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        cnt += 1
  return cnt

answer = [bfs(graph, i, k) for i in range(n) for k in range(n) if graph[i][k] == 1]
answer.sort()
print(len(answer))
print(*answer, sep = '\n')
