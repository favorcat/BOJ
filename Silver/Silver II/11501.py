import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  price = list(map(int, input().split()))
  res = 0
  cnt = 0
  
  for i in range(n-1, -1, -1):
    if price[i] > cnt:
      cnt = price[i]
    else:
      res += cnt - price[i]
  print(res)