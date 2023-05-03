import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(y, x):
  graph[y][x] = '.'
  for a, b in (1, 0), (-1, 0), (0, 1), (0, -1):
    Y, X = y + a, x + b
    if (0 <= Y < H) and (0 <= X < W) and (graph[Y][X] == '#'):
      dfs(Y, X)

T = int(input())
for _ in range(T):
  H, W = map(int,input().split())
  graph = [list(input().rstrip()) for _ in range(H)]
  cnt = 0
  
  for i in range(H):
    for k in range(W):
      if graph[i][k] == '#':
        dfs(i, k)
        cnt += 1

  print(cnt)