n = int(input())
a = list(map(int, input().split()))
m = int(input())

start, end = 0, max(a)
while start <= end:
  mid = (start + end) // 2
  total = 0
  for i in a: total += min(i, mid)
  
  if total > m: end = mid - 1
  else: start = mid + 1
print(end)
