import sys
input = sys.stdin.readline

n = int(input())
fix = list(input().rstrip())
num = [int(input()) for _ in range(n)]
stack = []

for i in fix:
  if 'A' <= i <= 'Z':
    stack.append(num[ord(i)-65])
  else:
    a = stack.pop()
    b = stack.pop()
    
    if i == '+':
      stack.append(b+a)
    elif i == '-':
      stack.append(b-a)
    elif i == '*':
      stack.append(b*a)
    elif i == '/':
      stack.append(b/a)

print('%.2f' %stack[0])