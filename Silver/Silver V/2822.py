score = []
total = 0
for i in range(8):
    score.append(int(input()))

sorted_score = sorted(score, reverse=True)
ans = []
for i in range(5):
    ans.append(score.index(sorted_score[i])+1)
    total += sorted_score[i]

ans.sort()
print(total)
for n in ans:
    print(n, end=' ')