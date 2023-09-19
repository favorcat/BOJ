n = int(input())
while True:
  flag = True
  for i in str(n):
    if i != '4' and i != '7':
      flag = False
      n -= 1
  if flag:
    print(n)
    break