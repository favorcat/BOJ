import math
m = 123456
arr = [True] * (2*m+1)
arr[0], arr[1] = False, False

for i in range(2, int(math.sqrt(2*m)+1)):
  if arr[i]:
    k = 2
    while(i * k <= 2*m):
      arr[i*k] = False
      k += 1

while(True):
  n = int(input())
  if n == 0: break
  cnt = 0
  
  for i in range(n+1, n*2+1):
    if arr[i]: cnt += 1
  print(cnt)
