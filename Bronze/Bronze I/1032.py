import sys
input = sys.stdin.readline

n = int(input())
s = ''
for i in range(n):
  a = input().rstrip()
  if i == 0:
    s = list(a)
  else:
    for k in range(len(s)):
      if a[k] != s[k]:
        s[k] = '?'

print("".join(s))
