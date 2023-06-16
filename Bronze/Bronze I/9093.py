import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
  sentence = list(map(str,input().split()))
  for s in sentence:
    print(s[::-1], end=" ")
  print()