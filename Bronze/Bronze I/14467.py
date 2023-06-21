import sys
input = sys.stdin.readline
n = int(input())
cow = [-1] * 11
cnt = 0

for _ in range(n):
  a, b = map(int,input().split())
  if cow[a] == -1:
    cow[a] = b
  elif cow[a] != b:
    cow[a] = b
    cnt += 1
print(cnt)