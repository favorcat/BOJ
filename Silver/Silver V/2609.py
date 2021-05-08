n, m = map(int,input().split())

i=1
while (i<=n and i<=m):
    if(n%i == 0 and m%i == 0):
        gcd = i
    i += 1

i = n if n>m else m
while True:
    if(i%n == 0 and i%m == 0):
        lcm = i
        break
    i += 1
    
print(gcd)
print(lcm)