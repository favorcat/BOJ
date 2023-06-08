import sys
input = sys.stdin.readline
s = input()
cnt = 0
stack = []

for i in range(len(s)):
  if s[i] == '(':
    stack.append('(')
  elif s[i] == ')':
    if s[i-1] == '(':
      stack.pop(-1)
      cnt += len(stack)
    else:
      stack.pop(-1)
      cnt += 1
print(cnt)