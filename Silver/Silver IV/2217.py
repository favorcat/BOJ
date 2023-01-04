n = int(input())
k = []
for i in range(n):
    m = int(input())
    k.append(m)
k.sort(reverse=True)
print(k)
res = 0
for i in range(n):
    if res < k[i]*(i+1): res = k[i]*(i+1)
print(res)