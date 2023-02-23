xa = int(input())
yb = int(input())
yc = int(input())
yd = int(input())
p = int(input())

x = xa * p
y = yb
if p > yc:
  y += (p - yc) * yd

print(min(x, y))
