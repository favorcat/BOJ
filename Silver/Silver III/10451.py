def dfs(v):
  visited[v] = 1
  next = li[v]
  if visited[next] == 0: dfs(next)

t = int(input())
for _ in range(t):
  n = int(input())
  li = [0] + list(map(int,input().split()))
  visited = [0] * (n+1)
  ans = 0
  
  for i in range(1, n+1):
    if visited[i] == 0:
      dfs(i)
      ans += 1
  print(ans)