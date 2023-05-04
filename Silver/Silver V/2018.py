import sys
input = sys.stdin.readline
n = int(input())

cnt, tmp = 0, 1
start, end = 0, 1

while end <= n:
  if tmp < n:
    end += 1
    tmp += end
  elif tmp == n:
    cnt += 1
    end += 1
    tmp += end
  else:
    tmp -= start
    start += 1

print(cnt)