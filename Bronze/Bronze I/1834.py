n = int(input())
result = 0
for i in range(n+1, n**2, n+1):
    result += i
print(result)