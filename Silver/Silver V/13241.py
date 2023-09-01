a, b = map(int,input().split())

def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a%b)

print(a*b // gcd(a,b))