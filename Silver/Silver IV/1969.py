import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dna = []
for _ in range(n):
  dna.append(input())

res = ''
distance = 0

for i in range(m):
  cnt = [0,0,0,0]
  for j in range(n):
    if dna[j][i] == 'A':
      cnt[0] += 1
    elif dna[j][i] == 'C':
      cnt[1] += 1
    elif dna[j][i] == 'G':
      cnt[2] += 1
    elif dna[j][i] == 'T':
      cnt[3] += 1
  
  idx = cnt.index(max(cnt))
  if idx == 0:
    res += 'A'
  elif idx == 1:
    res += 'C'
  elif idx == 2:
    res += 'G'
  elif idx == 3:
    res += 'T'
  distance += n - max(cnt)

print(res)
print(distance)