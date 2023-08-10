import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
  pw = input().rstrip()
  if len(pw) >= 6 and len(pw) <= 9:
    print('yes')
  else: print('no')