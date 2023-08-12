import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int,input().split()))
ans = [0] * n

for i in range(n):
  a = m[i]
  cnt = 0
  for k in range(n):
    if cnt == a and ans[k] == 0:
      ans[k] = i+1
      break
    elif ans[k] == 0:
      cnt += 1

for j in ans:
  print(j, end=" ")