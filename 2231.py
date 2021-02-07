N = int(input())
flag = False
for i in range(N):
    sum = 0
    sum += i
    k = i
    while k >= 1:
        j = k % 10
        sum += j
        k = k//10
    if N == sum:
        print(i)
        flag = True
        break
if not flag: print(0)
