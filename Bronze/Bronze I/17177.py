import math
a, b, c = map(int,input().split())
r1 = a*a - b*b
r2 = a*a - c*c
d = int((math.sqrt(r1*r2) - b*c) / a)
if d > 0: print(d)
else: print(-1)