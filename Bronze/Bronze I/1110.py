n = int(input())
count = 0

k = n
while True:
    if k < 10:
        a = 0
        b = k
    else:
        a = k // 10
        b = k % 10
    c = a + b
    if c < 10:
        k = b * 10 + c
    else: k = b * 10 + c % 10
    count += 1
    if k == n: break
print(count)