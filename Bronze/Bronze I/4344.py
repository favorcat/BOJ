c = int(input())
for i in range(c):
  n = list(map(int,input().split()))
  avg = sum(n[1:])/n[0]
  cnt = 0
  for k in n[1:]:
    if k > avg : cnt += 1
  res = cnt/n[0]*100
  print(f"{res:0.3f}%")
