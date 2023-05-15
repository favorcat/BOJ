import math
import sys
input = sys.stdin.readline
n = int(input())

def isPrime(a):
  if a < 2:
    return False
  for i in range(2, int(math.sqrt(a))+1):
    if a % i == 0:
      return False
  return True

def dfs(b):
  if len(str(b)) == n:
    print(b)
  else:
    for i in range(10):
      tmp = b * 10 + i
      if isPrime(tmp):
        dfs(tmp)

dfs(2)
dfs(3)
dfs(5)
dfs(7)