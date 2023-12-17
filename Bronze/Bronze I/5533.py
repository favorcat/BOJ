n = int(input())
player = [[],[],[]]
for _ in range(n):
  a,b,c = map(int,input().split())
  player[0].append(a)
  player[1].append(b)
  player[2].append(c)

score = [0] * n
for i in range(3):
    for j in range(n):
      if player[i].count(player[i][j]) >= 2:
        score[j] += 0
      else:
        score[j] += player[i][j]
print(*score, sep='\n')