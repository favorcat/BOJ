import sys
input = sys.stdin.readline
n = int(input())
ring = list(map(int,input().split()))

def rot(x, y):
  while(y != 0):
    tmp = x % y
    x = y
    y = tmp
  return x

for i in range(1, n):
  m = rot(ring[0], ring[i])
  print(f"{ring[0]//m}/{ring[i]//m}")