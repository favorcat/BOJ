import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
  for _ in range(i):
    print(" ", end="")
  k = (2*n)-1-(i*2)
  for _ in range(k):
    print("*", end="")
  print()
  
for i in range(n-2, -1, -1):
  for _ in range(i):
    print(" ", end="")
  k = (2*n)-1-(i*2)
  for _ in range(k):
    print("*", end="")
  print()