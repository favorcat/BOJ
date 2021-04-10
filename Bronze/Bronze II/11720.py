N = int(input())
M = list(map(int,input()))
res = 0
for i in range(N):
    res += M[i]
print(res)