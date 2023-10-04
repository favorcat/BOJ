n = int(input())
for _ in range(n):
    a,b,x = map(int, input().split())
    print(a*(x-1)+b)