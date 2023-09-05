from itertools import combinations
n = int(input())
ans = []

for i in range(1, 11):
  for j in combinations(range(10), i):
    a = ''.join(list(map(str,reversed(list(j)))))
    ans.append(int(a))
ans.sort()
if n >= len(ans):
  print(-1)
else:
  print(ans[n])