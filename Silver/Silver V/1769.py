import sys
x = list(sys.stdin.readline().rstrip())
y = ''
for i in range(len(x)):
    y += x[i]
cnt = 0

if len(x) > 1:
    while True:
        x = str(y)
        y = 0
        for i in range(len(x)):
            y += int(x[i])
        cnt += 1
        if y < 10:
            x = y
            break
else:
    y = int(y)

print(cnt)
if y in [3, 6, 9]: print('YES')
else: print('NO')