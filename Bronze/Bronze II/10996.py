import sys
input = sys.stdin.readline
n = int(input())

for i in range(n*2):
  for k in range(n):
    if i % 2 == 0:  a = k
    else:           a = k + 1
    if a % 2 == 0:
      print("*", end="")
    else:
      print(" ", end="")
  print()
