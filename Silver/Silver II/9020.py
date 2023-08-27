import math
def is_prime(n):
  if n == 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n%i == 0:
      return False
  return True

t = int(input())
for _ in range(t):
  n = int(input())
  a = n // 2
  b = n // 2
  
  while a > 0:
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1