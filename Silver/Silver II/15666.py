n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []

def backtracking(depth):
  if depth == m:
    print(" ".join(map(str,ans)))
    return
  b = 0
  for i in range(n):
    if b != a[i] and (depth == 0 or ans[-1] <= a[i]):
      ans.append(a[i])
      b = a[i]
      backtracking(depth+1)
      ans.pop()

backtracking(0)
