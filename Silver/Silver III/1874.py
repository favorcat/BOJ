n = int(input())
m = 0
check = 1
stack = []
result = []

for i in range(n):
    num = int(input())
    while m < num:
        m += 1
        stack.append(m)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        check = 0
        break

if check == 0:
    print('NO')
else:
    for cal in result:
        print(cal)