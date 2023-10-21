import sys
input = sys.stdin.readline

s = list(input().rstrip())
m = int(input())
tmp = []
for _ in range(m):
  cmd = list(input().split())
  if cmd[0] == 'L':
    if s: tmp.append(s.pop())
  elif cmd[0] == 'D':
    if tmp: s.append(tmp.pop())
  elif cmd[0] == 'B':
    if s: s.pop()
  elif cmd[0] == 'P':
    s.append(cmd[1])
print(''.join(s+list(reversed(tmp))))