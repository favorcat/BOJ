n = int(input())

for i in range(n):
  a = n-i-1
  for j in range(a):
    print(" ",end="")
  for k in range(2*i+1):
    print("*",end="")
  print()
for i in range(n-1):
  a = n-i-1
  for k in range(i+1):
    print(" ",end="")
  for j in range(a*2-1):
    print("*",end="")
  print()
