n, m = map(int, input().split())
ans = 0

if n == 1:
  ans = 1

elif n == 2: 
  if m >= 1 and m <= 6:
    ans = (m + 1) // 2 
  elif m >= 7:
    ans = 4

elif n >= 3: 
  if m <= 6:
    ans = min(m, 4)
  elif m >= 7:
    ans = m - 2

print(ans)