li = list(map(int,input().split()))
ans = [1,2,3,4,5]
while True:
  for i in range(len(li)-1):
    if li[i] > li[i+1]:
      li[i], li[i+1] = li[i+1], li[i]
      print(*li, sep=" ")
  if li == ans: break