x = int(input())
stick = 64
cnt = 0
total = 0

if x == 64:
  print(1)
else:
  while stick != 0:
    stick = stick//2
    if (stick+total) <= x:
      total += stick
      cnt += 1

  print(cnt-1)
