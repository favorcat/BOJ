import re
n = int(input())
p = re.compile('.*'.join(input().split('*')))

for _ in range(n):
  s = input()
  if p.fullmatch(s): print('DA')
  else: print('NE')