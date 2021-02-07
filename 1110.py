n = int(input())
count = 0
k = n
while True:
    a = k // 10
    b = k % 10
    new = (10*b + (a+b)) % 10
    k = 10*b+new
    count += 1
    if k < 10:
        break
print(count)
