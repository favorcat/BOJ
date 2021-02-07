n, m = map(int,input().split())
li = list(map(int,input().split()))
s = n*m
for i in range(5):
    print(li[i]-s, end=' ')
