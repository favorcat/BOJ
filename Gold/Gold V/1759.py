import sys
input = sys.stdin.readline
from itertools import combinations

l,c = map(int,input().split())
s = list(map(str,input().split()))
s.sort()

comb = list(combinations(s,l))
for a in comb:
  cnt = 0
  for i in a:
    if i in 'aeiou':
      cnt += 1
  if cnt >= 1 and cnt <= l-2:
    print(''.join(a))