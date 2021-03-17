n, k = map(int,input().split())
total = k
for i in range(n):
    plus, minus = map(int,input().split())
    total += plus
    total -= minus
    if i == n-1:
        total = 0
print("비와이")
