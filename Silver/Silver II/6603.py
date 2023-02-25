from itertools import combinations

while True:
  s = list(map(int,input().split()))
  if s[0] == 0: break
  k = s[0]
  del s[0]
  
  s = list(combinations(s,6))
  for i in s:
    for k in i:
      print(k,end=' ')
    print()
  print()