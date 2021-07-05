n = int(input())
m = n % 5
cnt = 0
if (n == 1) or (n == 3):
    print(-1)
elif m % 2 == 0:
    print(n//5 + m//2)
else:
    print((n//5)-1 + (m+5)//2)