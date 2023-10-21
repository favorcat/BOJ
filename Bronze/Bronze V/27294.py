t,s = map(int,input().split())
if (0 <= t < 12) or (16 < t <= 23) or s==1:
  print(280)
else: print(320)