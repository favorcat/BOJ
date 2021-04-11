N, X = map(int,input().split())
A = list(map(int,input().split()))
res = []
for i in range(N):
    if (A[i] < X): res.append(A[i])
for k in range(len(res)):
    print(res[k], end=' ')