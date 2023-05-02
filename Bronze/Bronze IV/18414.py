import sys
input = sys.stdin.readline

x,l,r = map(int,input().split())
res = l
m = abs(l-x)

for i in range(l,r+1):
  if abs(i-x) < m:
    m = abs(i-x)
    res = i
print(res)