import sys
input = sys.stdin.readline
s = input().rstrip()
l = len(s)

flag = 0
for i in range(l//2):
  if s[i] != s[l-i-1]:
    flag = 1
    break
if flag: print(0)
else: print(1)