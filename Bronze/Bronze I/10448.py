t = int(input())
tri = [n * (n+1)//2 for n in range(1,46)]
li = [0] * 1001
for i in tri:
  for k in tri:
    for j in tri:
      tmp = i + k + j
      if tmp <= 1000:
        li[tmp] = 1
for _ in range(t):
  k = int(input())
  print(li[k])