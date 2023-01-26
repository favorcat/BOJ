n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def backtracking(depth):
  if depth == m:
    print(" ".join(map(str,ans)))
    return
  for i in range(n):
    if a[i] in ans:
      continue
    ans.append(a[i])
    backtracking(depth+1)
    ans.pop()

backtracking(0)
