a = list(map(int,input().split()))
ans = min(a)
while True:
  cnt = 0
  for i in a:
    if ans % i == 0:
      cnt += 1
  if cnt > 2:
    break
  ans += 1
print(ans)