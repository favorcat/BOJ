from itertools import permutations
import sys
input = sys.stdin.readline
a, b = map(str, input().split())
c = -1

li = []
for i in permutations(a):
  li.append(''.join(i))

for n in li:
  if n[0] == '0':
    continue
  n = int(n)
  if n < int(b):
    c = max(c, n)

print(c)