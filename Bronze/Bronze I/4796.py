cnt = 0
while True:
  L, P, V = map(int, input().split())
  if L == 0 and P == 0 and V == 0: break
  ans = 0
  day = P - L
  flag = 0
  
  while V > 0:
    if flag == 0:
      if V >= L:
        ans += L
        V -= L
      else:
        ans += V
        V -= V
      flag = 1
    else:
      if V >= day:
        V -= day
      else:
        V -= V
      flag = 0
  cnt += 1
  print("Case", end=" ")
  print(cnt, end="")
  print(":", end=" ")
  print(ans)
