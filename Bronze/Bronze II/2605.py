import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int,input().split()))
res = [1]

for i in range(1,n):
  res.insert(len(res)-m[i], i+1)

for a in res:
  print(a, end=" ")