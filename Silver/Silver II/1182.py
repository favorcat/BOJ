n, s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0

def backtracking(idx, sum):
  global cnt
  if idx >= n:
    return
  
  sum += arr[idx]
  if sum == s:
    cnt += 1
  backtracking(idx+1, sum-arr[idx])
  backtracking(idx+1, sum)

backtracking(0, 0)
print(cnt)
