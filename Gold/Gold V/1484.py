g = int(input())
left = 1
right = 1
ans = []

while True:
  tmp = right**2 - left**2
  if right-left == 1 and tmp > g: break
  if tmp > g: left += 1
  elif tmp < g: right += 1
  else:
    ans.append(right)
    right += 1

if ans: print(*ans, sep='\n')
else: print(-1)