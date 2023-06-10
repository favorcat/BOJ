import math
import sys
input = sys.stdin.readline
n = int(input())

def is_prime_num(n):
  if n in [0, 1]:
      return False
  for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
          return False
  return True

def is_palindrome(n):
  return str(n) == str(n)[::-1]

ans = 0
for i in range(n, 1000001):
  if is_palindrome(i) and is_prime_num(i):
    ans = i
    break
if ans == 0: ans = 1003001
print(ans)