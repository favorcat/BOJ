n = int(input())
a = []

for i in range(n):
    k = n
    count = 0
    while True:
        if k == 1:
            break
        if k % 3 == 0:
            k = k//3
        if k % 3 == 1:
            n -= 1
        if k % 2 == 0:
            k = k//2
        else: k -= 1
        count += 1
    a[i] = count
print(a)
