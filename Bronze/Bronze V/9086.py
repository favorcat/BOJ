T = int(input())
for _ in range(T):
  s = input()
  if len(s) == 0: print(s+s)
  else:
    print(s[0]+s[-1])
