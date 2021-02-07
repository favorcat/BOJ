a, b, n, w = map(int,input().split())
an = 0

for i in range(1, n):
    if a * i + b * (n-i) == w:
        if an == 0:
            an = i
        else: an = -1

if an > 0:
    print(an, n-an)
else:
    print(-1)