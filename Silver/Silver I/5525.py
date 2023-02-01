import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

start, end = 0, 0
cnt = 0

while end < m:
  if s[end:end+3] == "IOI":
    end += 2
    if end - start == n*2:
      cnt += 1
      start += 2
  else:
    start = end = end + 1
print(cnt)
