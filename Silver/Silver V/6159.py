import sys
input = sys.stdin.readline
n, s = map(int,input().split())
cow = [int(input()) for _ in range(n)]
ans = 0

for i in range(n-1):
  for k in range(i+1, n):
    if cow[i]+cow[k] <= s:
      ans += 1
print(ans)