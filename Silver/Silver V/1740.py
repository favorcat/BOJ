n = bin(int(input()))[2:]
result = 0
for i in range(len(n)):
    if int(n[i]) == 1:
        result += 3 ** (len(n)-1-i)
print(result)