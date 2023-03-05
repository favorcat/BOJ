dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
def bfs(x, y):
  m[x][y] = 0
  q = [[x, y]]
  while q:
    a, b = q[0][0], q[0][1]
    del q[0]
    for i in range(8):
      x = a+dx[i]
      y = b+dy[i]
      if 0 <= x < h and 0 <= y < w and m[x][y] == 1:
        m[x][y] = 0
        q.append([x, y])

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  m = []
  cnt = 0
  for _ in range(h):
    m.append(list(map(int,input().split())))

  for i in range(h):
    for j in range(w):
      if m[i][j] == 1:
        bfs(i, j)
        cnt += 1

  print(cnt)
