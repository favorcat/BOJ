n = int(input())
li = map(int,input().split())
a, b = 0, 0
for i in li:
  if i % 2 == 0:
    a += 1
  else:
    b += 1
if a > b: print('Happy')
else: print('Sad')