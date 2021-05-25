n, k = map(int,input().split())
arr = [i for i in range(1, n+1)]
print('<', end='')

for j in range(n):
    for i in range(k-1):
        arr.append(arr.pop(0))
    if (j != n-1):
        print(arr.pop(0), end=', ')
    else: print(arr.pop(0), end='')
print('>', end=' ')