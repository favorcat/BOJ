n = int(input())
num = 1
plus = 6
result = 1

if n == 1:
    print(result)
else:
    while n > num:
        num += plus
        result += 1
        plus += 6
    print(result)