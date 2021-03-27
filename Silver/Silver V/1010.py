t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    result = 1
    for k in range(n):
        result *= (m-k)
        result //= k+1
    print(result)