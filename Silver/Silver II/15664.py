n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
ans = []
arr = [0]*n

def backtracking(depth):
  if depth == m:
    print(" ".join(map(str,ans)))
    return
  b = 0
  for i in range(n):
    if not arr[i] and b != a[i] and (depth == 0 or ans[-1] <= a[i]):
      arr[i] = 1
      ans.append(a[i])
      b = a[i]
      backtracking(depth+1)
      arr[i] = 0
      ans.pop()

backtracking(0)