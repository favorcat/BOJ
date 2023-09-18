import sys
input = sys.stdin.readline

prime = list(range(1000001))
for i in range(2, 1001):
  if prime[i]: prime[i+i::i] = [0] * len(prime[i+i::i])
prime = list(filter(lambda x: x != 0, prime[3:]))
prime_set = set(prime)

while True:
  n = int(input())
  if n == 0: break
  for a in prime:
    b = n - a
    if b in prime_set:
      print(f'{n} = {a} + {b}')
      break
  else: print("Goldbach's conjecture is wrong.")