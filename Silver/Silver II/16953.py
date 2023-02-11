a, b = map(int,input().split())
cnt = 1

while a != b:
  cnt += 1
  if a == b:
    break
  
  tmp = b
  if b % 10 == 1:
    b //= 10
  elif b % 2 == 0:
    b //= 2
  
  if tmp == b:
    cnt = -1
    break

print(cnt)
