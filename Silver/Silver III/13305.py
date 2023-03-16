import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
m = price[0]
res = 0

for i in range(n-1):
  if m > price[i]:
    m = price[i]
  res += m * distance[i]
print(res)
