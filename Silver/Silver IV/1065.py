N = int(input())
result = 0
for i in range(1, N+1):
    if i <= 99:
        result += 1
    else:
        number = list(map(int,str(i)))
        if number[0] - number[1] == number[1] - number[2]:
            result += 1
print(result)