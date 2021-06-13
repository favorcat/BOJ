M = int(input())
N = int(input())

min_num = 0
result = 0

for i in range(M, N+1):
    if i != 1:
        chk = 0
        for k in range(2, i):
            if i%k == 0:
                chk = 1
                break
        if chk == 0:
            if min_num == 0:
                min_num = i
            result += i

if result == 0:
    print(-1)
else:
    print(result)
    print(min_num)