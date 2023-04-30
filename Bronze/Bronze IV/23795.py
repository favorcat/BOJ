import sys
input = sys.stdin.readline

cnt = 0
while(True):
  n = int(input())
  if n == -1: break
  cnt += n
print(cnt)