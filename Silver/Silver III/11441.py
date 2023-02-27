import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
s = [0]
for i in range(n):
  s.append(s[i]+a[i])

m = int(input())
for _ in range(m):
  i, j = map(int,input().split())
  print(s[j]-s[i-1])
