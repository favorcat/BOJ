n = int(input())
for i in range(n):
    vps = list(input())
    sum = 0
    for k in range(len(vps)):
        if (vps[k] == '('):
            sum += 1
        elif (vps[k] == ')'):
            sum -= 1
        if (sum < 0):
            break
    if (sum == 0):
        print('YES')
    else: print('NO')