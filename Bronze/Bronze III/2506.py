n = int(input())
result = list(map(int,input().split()))
score = 0
sum = 0
for i in range(n):
    add = 1
    if result[i] == 1:
        sum += 1
        score += sum
    else:
        sum = 0

print(score)