import sys
input = sys.stdin.readline
n = int(input())

line = 1
while n>line:
  n -= line
  line += 1
if line%2 == 0:
  a=n
  b=line-n+1
else:
  a=line-n+1
  b=n
print(a,'/',b,sep='')