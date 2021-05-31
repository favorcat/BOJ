n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key = lambda x: (x[1], x[0]))
for k in range(n):
    print(arr[k][0], arr[k][1])