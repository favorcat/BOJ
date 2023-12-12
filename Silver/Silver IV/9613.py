import math
t = int(input())
for _ in range(t):
  n = list(map(int,input().split()))
  ans = 0
  for i in range(1, len(n)):
    for j in range(i+1, len(n)):
      ans += math.gcd(n[i], n[j])
  print(ans)