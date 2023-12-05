n = int(input())
ban = [list(map(int,input().split())) for _ in range(n)]
same = [[0]*n for _ in range(n)]

for i in range(5):
  for j in range(n):
    for k in range(j+1, n):
      if ban[j][i] == ban[k][i]:
        same[k][j] = 1
        same[j][k] = 1

cnt = []
for a in same:
  cnt.append(a.count(1))
print(cnt.index(max(cnt))+1)