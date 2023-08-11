import sys
input = sys.stdin.readline
n = int(input())
li = [input().rstrip() for _ in range(n)]

for s in li:
  if s[::-1] in li:
    print(len(s), end=" ")
    print(s[len(s)//2])
    break