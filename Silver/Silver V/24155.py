n = int(input())
score = []
for i in range(n):
    m = int(input())
    score.append([i, m, 0])

tmp = 0
idx = 0
cnt = 0
sscore = sorted(score, key=lambda x: x[1], reverse=True)
for j in range(n):
    flag = 1
    if tmp == sscore[j][1]:
        sscore[j][2] = idx
        flag = 0
    cnt += 1
    if flag:
        idx = cnt
        sscore[j][2] = idx
    tmp = sscore[j][1]

ans = sorted(sscore, key=lambda x: x[0])
for a in ans:
    print(a[2])
