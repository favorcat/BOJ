n = int(input())
score = list(map(int,input().split()))
max_score = max(score)
avg = 0
for i in range(n):
    score[i] = score[i]/max_score*100
    avg += score[i]
avg /= n
print(avg)