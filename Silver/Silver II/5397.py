import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
  L = input().rstrip()
  left = []
  right = []
  
  for i in L:
    if i == '-':
      if left:
        left.pop()
    elif i == '<':
      if left:
        right.append(left.pop())
    elif i == '>':
      if right:
        left.append(right.pop())
    else:
      left.append(i)
  left.extend(reversed(right))
  print(''.join(left))