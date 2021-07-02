import math
M, N = map(int,input().split())
arr = []
for i in range(M, N+1):
    if i != 1:
        chk = 0
        for k in range(2, int(math.sqrt(i))+1):
            if i % k == 0:
                chk = 1
                break
        if chk == 0:
            arr.append(i)

for num in arr:
    print(num)