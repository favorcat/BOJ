import sys
input = sys.stdin.readline
a,b = map(int,input().split())
c,d = map(int,input().split())

def gcd(x, y):
  mod = x % y
  while mod > 0:
    x = y
    y = mod
    mod = x % y
  return y

n = gcd(a*d + c*b, b*d)
print( (a*d + c*b)//n, b*d//n )