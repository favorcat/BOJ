n = int(input())
person = []
for i in range(n):
    x, y = map(int,input().split())
    person.append((x, y))

rank = [1 for i in range(n)]

for i in range(n):
    for k in range(n):
        if i != k:
            if person[i][0] < person[k][0] and person[i][1] < person[k][1]:
                rank[i] += 1
                
for i in range(n):
    if i != n-1:
        print(rank[i], end=' ')
    else: print(rank[i])