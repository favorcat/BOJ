T = int(input())
for i in range(T):
  n, m = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort()
  b.sort()
  
  idx = 0
  cnt = 0
  for k in range(n):
    while True:
      if idx == m or a[k] <= b[idx]:
        cnt += idx
        break
      else: idx += 1
  print(cnt)
