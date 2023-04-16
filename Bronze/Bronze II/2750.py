import sys
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(key=lambda x: x)
for a in arr:
  print(a)