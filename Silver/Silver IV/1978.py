n = int(input())
arr = list(map(int,input().split()))
cnt = 0
for i in arr:
    arrcnt = 0
    if (i >= 2):
        for k in range(2, i+1):
            if (i % k == 0): arrcnt+= 1
        if (arrcnt == 1):
            cnt+=1
print(cnt)