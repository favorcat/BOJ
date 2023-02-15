from itertools import combinations

def isPrime(n):
  i = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

n, m = map(int,input().split())
h = list(map(int,input().split()))

c = list(combinations(h,m))
ans = []

for a in c:
  total = sum(a)
  if isPrime(total):
    ans.append(total)

ans = sorted(list(set(ans)))
if len(ans) == 0:
  print(-1)
else:
  for i in ans:
    print(i, end=" ")
