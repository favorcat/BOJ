import math
import sys
input = sys.stdin.readline
a, b = map(int,input().split())

def is_prime_num(n):
  for i in range(2, int(math.sqrt(n))+1):
      if n % i == 0:
        d[n] = d[n//i] + 1
        return False
  d[n] = 1
  return True

d = [0] * (b+1)
prime = [False] * (b+1)
for i in range(2, b+1):
  prime[i] = is_prime_num(i)
  
ans = 0
for i in range(a, b+1):
  ans += prime[d[i]]
print(ans)