n = int(input())
a = [i for i in range(1,n+1)]
ans = []

def backtracking(depth):
  if depth == n:
    print(" ".join(map(str,ans)))
    return
  for i in range(n):
    if a[i] in ans:
      continue
    ans.append(a[i])
    backtracking(depth+1)
    ans.pop()

backtracking(0)
