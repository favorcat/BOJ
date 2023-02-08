import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

ans = 0
cnt = 0
tmp = 0

for i in range(n):
  if tmp < a[i] :
    tmp = a[i]
    cnt = 0
  else:
    cnt += 1
  ans = max(ans, cnt)

print(ans)
