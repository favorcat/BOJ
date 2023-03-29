import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [input().rstrip() for _ in range(n)]
check = [input().rstrip() for _ in range(m)]
cnt = 0

for a in check:
  if a in s:
    cnt += 1

print(cnt)