import sys
input = sys.stdin.readline
n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()

ans = 5
for i in range(n):
  cnt = 0
  for k in range(li[i], li[i]+5):
    if k not in li:
      cnt += 1
  ans = min(ans, cnt)
print(ans)