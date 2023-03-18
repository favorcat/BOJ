import sys
import math
input = sys.stdin.readline
a, b = map(int, input().split())

if b > 10000000:
  b = 10000000

def is_prime_num(n):
  if n in [0, 1]:
      return False
  for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
          return False
  return True

def is_palindrome(n):
  return str(n) == str(n)[::-1]

for i in range(a, b+1):
  if is_palindrome(i):
    if is_prime_num(i): print(i)
print(-1)
