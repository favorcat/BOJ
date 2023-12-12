a, b = map(str,input().split())
la, lb = len(a), len(b)
ans = [['.']*la for _ in range(lb)]

for i in range(la):
  flag = 0
  for j in range(lb):
    if a[i] == b[j]:
      row = j
      col = i
      flag = 1
      break
  if flag: break

for i in range(la):
  ans[row][i] = a[i]
for j in range(lb):
  ans[j][col] = b[j]
for i in range(lb):
  print(''.join(ans[i]))