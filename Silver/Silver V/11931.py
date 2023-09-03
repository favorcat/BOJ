import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
for i in a:
  print(i)