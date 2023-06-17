import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  n, m = map(int,input().split())
  cnt = 0
  for i in range(n, m+1):
    cnt += str(i).count('0')
  print(cnt)