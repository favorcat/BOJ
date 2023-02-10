n = int(input())
a = 2
while n != 1:
  if n % a == 0:
    print(a)
    n = n // a
  else:
    a += 1
