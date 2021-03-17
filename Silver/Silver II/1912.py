n = int(input())
m = list(map(int,input().split()))
s = 0
mx = -1000
for i in range(n):
    s += m[i]
    mx = max(mx,s)
    if s <= 0:
        s = 0
print(mx)
